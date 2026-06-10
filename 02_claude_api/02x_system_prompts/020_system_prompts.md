---
title: "Building with the Claude API · System Prompts"
authors: ["John Mario Montoya Zapata"]
date: "29/04/2026"
updated: ""
course: "Building with the Claude API"
module: "Fundamentos de la API"
lecture: "System Prompts"
stage: "Básico"
status: "borrador"
tags: ["claude-api", "system-prompt", "rol", "comportamiento", "personalización"]
links:
  - "[[INDEX]]"
  - "[[02_claude_api/_overview]]"
  - "[[01_fundamentos_api_y_conversaciones]]"
  - "[[19_structure_with_xml_tags]]"
---

# System Prompts

> **Resumen Feynman (una frase):** El system prompt es una instrucción de "rol y
> comportamiento" que se le da al modelo antes de la conversación — controla el *cómo*
> responde, no el *qué* responde.

---

## 1) Analogía sencilla

Antes de que un empleado nuevo atienda clientes, le das un briefing: "Eres el tutor de
matemáticas de este estudiante. Tu rol es guiar con pistas, no dar la respuesta directa.
Sé paciente y usa ejemplos sencillos."

Ese briefing no le dice qué preguntas harán los clientes — le dice cómo debe comportarse
independientemente de la pregunta. Eso es el system prompt.

---

## 2) ¿Qué es realmente?

El system prompt es un string que se pasa como argumento separado `system` en el request.
No va dentro de la lista `messages` — va en su propio campo.

**Propósito:** Controlar el *approach* de la respuesta, no el contenido.

```python
system_prompt = """You are a patient math tutor working with high school students.
Your role is to guide students toward understanding rather than giving direct answers.
When asked to solve a problem, provide hints and ask guiding questions instead."""

message = client.messages.create(
    model=MODEL,
    max_tokens=1000,
    system=system_prompt,       # ← campo separado, no va en messages
    messages=[
        {"role": "user", "content": "¿Cuánto es la derivada de x²?"}
    ]
)
# Con system prompt: "¿Recuerdas la regla de la potencia? ¿Qué le pasa al exponente?"
# Sin system prompt: "La derivada de x² es 2x."
```

---

## 3) ¿Cómo funciona? (mecanismo interno)

El system prompt se procesa antes que los mensajes del usuario. Claude lo usa como
marco de referencia para todas sus respuestas en la conversación.

**Patrón de implementación con condicional:**

```python
def chat(messages: list, system: str = None) -> str:
    params = {
        "model": MODEL,
        "max_tokens": 1000,
        "messages": messages,
    }
    if system:
        params["system"] = system   # Solo se agrega si existe
    return client.messages.create(**params).content[0].text
```

**Por qué el condicional:** Si pasas `system=None` explícitamente a la API, puede
causar errores en algunos SDKs. Mejor excluir la clave completamente cuando no aplica.

---

## 4) ¿Cuándo usarlo?

| Usar system prompt para | No usar para |
|------------------------|-------------|
| Asignar un rol específico | Datos específicos de la tarea (van en messages) |
| Definir tono y estilo | Instrucciones que cambian por request |
| Establecer restricciones permanentes | Contexto que depende del usuario |
| Formato de respuesta esperado | |

---

## 5) Ejemplo práctico mínimo

```python
# Asistente de análisis de datos para Protección
SYSTEM = """You are a senior data analyst specializing in pension fund data.
You work with BigQuery, Python, and Apache Airflow.
Always provide SQL examples when relevant.
Be concise and technical — the user is an experienced data scientist."""

response = chat(messages, system=SYSTEM)
```

---

## 6) Conexiones con otros conceptos

- `→ requiere:` [[01_fundamentos_api_y_conversaciones]] — el system prompt es un parámetro adicional al request base.
- `→ contrasta:` [[01_agent_skills/01_que_son_skills]] — los skills en Claude Code son el equivalente en el CLI; el system prompt es el equivalente en la API.
- `→ extiende:` [[19_structure_with_xml_tags]] — los XML tags en system prompts mejoran la comprensión de instrucciones complejas.
- `→ aplica en:` [[17_being_clear_and_direct]] — las técnicas de prompt engineering aplican también al system prompt.

---

## 7) Preguntas Feynman

1. ¿Cuál es la diferencia entre poner instrucciones en el system prompt vs. en el primer mensaje del usuario?
2. ¿El system prompt se incluye en el conteo de tokens de input? ¿Qué implicación tiene eso en el costo?
3. Tienes una app donde diferentes usuarios necesitan diferentes roles de Claude (tutor, analista, redactor). ¿Cómo manejarías el system prompt?

---

## 8) Tarjetas Anki

**Q:** ¿Dónde se pasa el system prompt en un request a la Claude API?
**A:** Como argumento separado `system=` en `client.messages.create()`, no dentro de la lista `messages`.

**Q:** ¿Qué controla el system prompt: el *qué* o el *cómo* responde Claude?
**A:** El *cómo* — el approach, tono, rol y comportamiento. El contenido específico lo determina la pregunta del usuario.

---

## 9) Lo que no es obvio

**El system prompt sí consume tokens de input y se cobra.**
Es parte del contexto que el modelo procesa. En aplicaciones con muchos requests, un
system prompt largo puede incrementar el costo significativamente. Aquí es donde el
prompt caching tiene impacto real.

**No todo debe ir en el system prompt.**
Es tentador meter toda la "personalidad" ahí. Pero instrucciones de tarea específica,
datos del usuario, o contexto que cambia por request deben ir en `messages`, no en
`system`. El system prompt es para invariantes de comportamiento.

---

## Notebooks de práctica

| Notebook | Qué cubre |
|----------|----------|
| [021_system_prompt.ipynb](021_system_prompt.ipynb) | Implementación del parámetro `system=` · función `chat()` con soporte condicional · prueba con tutor de matemáticas |

---

### Registro personal
- Qué conecta con mi trabajo: Es el equivalente de las instrucciones de inicialización de un agente en Vertex AI Agent Builder.
- Dudas abiertas: ¿Se puede cambiar el system prompt en medio de una conversación multi-turno o solo aplica al inicio?
- Siguientes pasos: Aprender sobre temperatura para controlar la aleatoriedad.
