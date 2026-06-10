---
title: "Building with the Claude API · Fundamentos: Modelos, Flujo y Conversaciones"
authors: ["John Mario Montoya Zapata"]
date: "29/04/2026"
updated: ""
course: "Building with the Claude API"
module: "Fundamentos de la API"
lecture: "Overview of Claude Models + Accessing the API + Making a Request + Multi-Turn Conversations"
stage: "Básico"
status: "borrador"
tags: ["claude-api", "modelos", "opus", "sonnet", "haiku", "tokens", "tokenización",
       "sdk", "python", "dotenv", "multi-turn", "historial", "stateless", "request"]
links:
  - "[[INDEX]]"
  - "[[02_claude_api/_overview]]"
  - "[[02_system_prompts]]"
  - "[[03_temperature]]"
  - "[[25_handling_message_blocks]]"
  - "[[27_multi_turn_with_tools]]"
  - "[[37_text_embeddings]]"
---

# Fundamentos de la API — Modelos, Flujo y Conversaciones

> **Resumen Feynman (una frase):** Para usar la Claude API necesitas elegir un modelo
> (Opus/Sonnet/Haiku según la tarea), enrutar siempre por tu servidor, construir el
> request con cuatro parámetros obligatorios, y gestionar tú mismo el historial porque
> la API es completamente stateless.

---

## 1) Analogía sencilla

Imagina un servicio de consultoría con tres perfiles de analistas y una recepcionista:

- **Opus** = consultor senior. Razonamiento profundo, multi-paso. Caro y lento.
- **Sonnet** = analista mid-level. Buen balance inteligencia/velocidad/costo. Ideal para coding.
- **Haiku** = analista junior rápido. Alto volumen, tiempo real. Sin razonamiento extendido.

Cuando un cliente (tu app) quiere una consulta, **nunca va directo al analista** — pasa
siempre por la recepcionista (tu servidor), quien lleva la solicitud con las credenciales
correctas. El analista procesa la pregunta en cuatro pasos internos (tokeniza → embedding
→ contextualiza → genera token a token) y devuelve la respuesta a la recepcionista.

El detalle clave: **el analista tiene amnesia total**. Si el cliente quiere una conversación
de ida y vuelta, la recepcionista debe llevar la transcripción completa de cada intercambio
anterior en cada nueva visita.

---

## 2) ¿Qué es realmente?

### 2a. Los tres modelos

| Modelo | Optimización | Casos de uso | Trade-off |
|--------|-------------|--------------|-----------|
| **Opus** | Inteligencia máxima | Razonamiento complejo, planificación multi-paso | Mayor costo y latencia |
| **Sonnet** | Balance inteligencia/velocidad/costo | Coding, análisis, mayoría de casos prácticos | El punto medio |
| **Haiku** | Velocidad y eficiencia | Interacciones en tiempo real, clasificación masiva | Sin razonamiento extendido |

**Framework de selección:**
```
¿Requiere razonamiento profundo o planificación multi-paso? → Opus
¿Es tarea masiva o necesita respuesta inmediata?           → Haiku
¿Nada de lo anterior?                                      → Sonnet (default)
```

### 2b. El flujo externo (5 pasos)

| Paso | Quién | Qué ocurre |
|------|-------|-----------|
| 1 | Cliente → Servidor | Usuario envía texto al servidor del developer |
| 2 | Servidor → Anthropic API | Request con API key + model + messages + max_tokens |
| 3 | Anthropic (interno) | Tokenización → Embedding → Contextualización → Generación |
| 4 | Anthropic (stop) | Para en max_tokens o token end_of_sequence |
| 5 | Anthropic → Servidor → Cliente | Response: texto + usage + stop_reason |

> **Seguridad crítica:** La API key NUNCA va en el cliente. Exponerla en código del browser
> permite a cualquiera hacer requests a tu costo desde los DevTools.

### 2c. El proceso interno de generación

| Etapa | Qué hace |
|-------|---------|
| **Tokenización** | Divide el input en tokens (palabras, partes, símbolos, espacios) |
| **Embedding** | Convierte cada token en un vector numérico con todos sus posibles significados |
| **Contextualización** | Ajusta los embeddings según tokens vecinos → determina significado preciso |
| **Generación** | Calcula probabilidades del siguiente token, selecciona (prob + aleatoriedad), repite |

### 2d. La API es completamente stateless

La API de Anthropic **no guarda ningún mensaje** entre requests. Cada llamada es
independiente. Para mantener conversaciones coherentes, el developer debe:
1. Mantener manualmente una lista de mensajes en su código
2. Enviar el historial completo en cada request

---

## 3) ¿Cómo funciona? (mecanismo interno)

```mermaid
flowchart TD
  subgraph "Request básico (un turno)"
    C[Cliente] -->|texto| S[Servidor]
    S -->|model + max_tokens + messages + api_key| A[Anthropic API]
    A -->|content[0].text + stop_reason + usage| S
    S --> C
  end

  subgraph "Multi-turno (historial manual)"
    H[Lista messages\nuser/assistant/user/...] --> S2[Servidor]
    S2 -->|historial COMPLETO| A2[Anthropic API]
    A2 --> R[Respuesta]
    R --> H
  end
```

**Setup mínimo:**

```python
# pip install anthropic python-dotenv
# .env → ANTHROPIC_API_KEY="sk-ant-..."  (agregar a .gitignore)

from dotenv import load_dotenv
import os, anthropic

load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
MODEL = "claude-sonnet-4-6"
```

**Request básico (un turno):**

```python
message = client.messages.create(
    model=MODEL,
    max_tokens=1000,                          # Límite de seguridad, no objetivo
    messages=[{"role": "user", "content": "¿Qué es un token?"}]
)
print(message.content[0].text)               # El texto generado
print(message.stop_reason)                   # "end_turn" o "max_tokens"
print(message.usage)                         # input_tokens + output_tokens
```

**Estructura del objeto de respuesta:**

```
Message(
  content = [ContentBlock(type="text", text="...")]  ← .content[0].text
  stop_reason = "end_turn" | "max_tokens" | "tool_use"
  usage = Usage(input_tokens=N, output_tokens=M)
)
```

**Multi-turno con historial manual:**

```python
def add_user_message(messages, text):
    messages.append({"role": "user", "content": text})

def add_assistant_message(messages, text):
    messages.append({"role": "assistant", "content": text})

def chat(messages):
    return client.messages.create(
        model=MODEL, max_tokens=1000, messages=messages
    ).content[0].text

# Flujo de conversación
messages = []
add_user_message(messages, "Mi nombre es John")
resp = chat(messages)
add_assistant_message(messages, resp)

add_user_message(messages, "¿Cómo me llamo?")
resp = chat(messages)       # Envía los 3 mensajes anteriores + este
add_assistant_message(messages, resp)
# Claude responde: "Te llamas John"
```

---

## 4) ¿Cuándo usar cada modelo?

| Tarea en Protección | Modelo recomendado |
|--------------------|-------------------|
| Clasificación masiva de transacciones | Haiku |
| Generación de reportes analíticos | Sonnet |
| Detección de patrones de riesgo complejos | Sonnet u Opus |
| Chatbot de atención rápida | Haiku |
| Análisis legal o de cumplimiento | Opus |

---

## 5) Ejemplo práctico integrado

```python
# Pipeline multi-modelo para Protección
MODELS = {
    "clasificacion": "claude-haiku-4-5-20251001",
    "analisis":      "claude-sonnet-4-6",
    "razonamiento":  "claude-opus-4-7",
}

def run_chat_session(system_prompt: str = None):
    """Sesión conversacional completa con historial"""
    messages = []
    params_base = {"model": MODELS["analisis"], "max_tokens": 1000}
    if system_prompt:
        params_base["system"] = system_prompt

    while True:
        user_input = input("Tú: ")
        if user_input.lower() == "salir":
            break
        add_user_message(messages, user_input)
        resp = client.messages.create(**params_base, messages=messages).content[0].text
        add_assistant_message(messages, resp)
        print(f"Claude: {resp}\n")
```

---

## 6) Conexiones con otros conceptos

- `→ extiende:` [[02_system_prompts]] — agrega el parámetro `system` al request base.
- `→ extiende:` [[03_temperature]] — agrega `temperature` para controlar aleatoriedad.
- `→ extiende:` [[27_multi_turn_with_tools]] — multi-turno con bloques de tool_use en el historial.
- `→ aplica en:` [[37_text_embeddings]] — los embeddings internos del modelo vs. embeddings externos para RAG.
- `→ aplica en:` [[14_model_based_grading]] — Haiku para evaluación de alto volumen.
- `→ contrasta:` [[01_agent_skills/01_que_son_skills]] — skills gestionan instrucciones; multi-turn gestiona historial de mensajes.

---

## 7) Preguntas Feynman

1. ¿Por qué el cliente (browser/mobile) nunca debe llamar directamente a la API? ¿Qué ataque concreto evita el servidor intermediario?
2. `max_tokens=500` pero Claude termina en 200 tokens. ¿Cuál es el `stop_reason` y cuánto se cobra?
3. ¿Por qué `messages` es una lista de dicts y no un simple string, incluso para un solo mensaje?
4. Tienes una conversación de 50 turnos. ¿Qué problema surge y qué estrategias tienes para resolverlo?
5. Un pipeline clasifica 500.000 registros al día. ¿Qué modelo eliges y por qué Haiku es mejor que Opus aquí aunque Opus sea "más inteligente"?

---

## 8) Tarjetas Anki

**Q:** ¿Cuáles son los 3 parámetros obligatorios en `client.messages.create()`?
**A:** `model`, `max_tokens`, y `messages`.

**Q:** ¿Cómo se accede al texto de la respuesta en un request básico?
**A:** `message.content[0].text`

**Q:** ¿La API de Anthropic guarda el historial entre requests?
**A:** No — es completamente stateless. El developer debe mantener y enviar el historial completo en cada request.

**Q:** ¿Qué indica `stop_reason: "end_turn"` vs `"max_tokens"`?
**A:** `"end_turn"` = Claude terminó naturalmente. `"max_tokens"` = alcanzó el límite antes de terminar.

**Q:** ¿Qué modelo usar para clasificación masiva de alto volumen en tiempo real?
**A:** Haiku — optimizado para velocidad y costo en tareas repetitivas.

**Q:** ¿Por qué los roles en el historial multi-turno deben alternarse user/assistant?
**A:** La API espera alternancia estricta. Dos mensajes del mismo rol seguidos causan error de validación.

---

## 9) Lo que no es obvio

**`max_tokens` es un techo de seguridad, no un objetivo.**
Claude para cuando termina naturalmente (end_of_sequence). Poner max_tokens=50 en una
tarea que necesita 200 tokens trunca la respuesta a mitad. Poner max_tokens=10000 no
hace que genere más — solo evita que nunca se corte.

**`content[0]` no es siempre seguro.**
Con tool use (→ [[25_handling_message_blocks]]), `content` tiene múltiples bloques
(texto + tool_use). Asumir `[0]` como texto rompe. Siempre verifica el tipo del bloque.

**El historial completo se cobra como tokens de input en cada request.**
Conversación de 10 turnos × historial promedio × costo por token = el costo se acumula
rápido. Estrategias: truncar mensajes viejos, resumir el historial con Haiku, o usar
prompt caching.

**"La memoria de Claude" es ilusoria — es tu lista `messages` quien recuerda.**
Si pierdes esa lista (reinicio de servidor, nueva sesión), la "memoria" desaparece.
Para persistencia real, guarda `messages` en una base de datos.

**Haiku sin razonamiento extendido ≠ Haiku sin capacidades.**
Haiku puede hacer tareas complejas de lenguaje. Lo que no puede es razonamiento
multi-paso encadenado (extended thinking). Para extracción simple, clasificación y
respuestas directas, es perfectamente capaz.

---

## Notebooks de práctica

| Notebook | Qué cubre |
|----------|----------|
| [011_requests.ipynb](011_requests.ipynb) | Setup del cliente · request básico · funciones helper · multi-turn programático · sesión de chat interactiva |

---

### Registro personal
- Qué conecta con mi trabajo: El patrón servidor-intermediario es idéntico a cómo manejo
  credenciales de BigQuery — nunca expuestas en el cliente, siempre en backend o
  Cloud Function. El historial stateless es igual a sesiones REST sin cookies de servidor.
- Dudas abiertas: ¿El prompt caching reduce el costo de enviar el historial completo
  repetidamente? ¿Los model IDs tienen aliases estables tipo "latest"?
- Siguientes pasos: System prompts y temperature para personalizar el comportamiento.
