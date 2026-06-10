---
title: "Building with the Claude API · Temperature"
authors: ["John Mario Montoya Zapata"]
date: "29/04/2026"
updated: ""
course: "Building with the Claude API"
module: "Fundamentos de la API"
lecture: "Temperature"
stage: "Básico"
status: "borrador"
tags: ["claude-api", "temperature", "aleatoriedad", "creatividad", "determinismo"]
links:
  - "[[INDEX]]"
  - "[[02_claude_api/_overview]]"
  - "[[01_fundamentos_api_y_conversaciones]]"
  - "[[08_controlling_model_output]]"
---

# Temperature

> **Resumen Feynman (una frase):** Temperature (0 a 1) controla cuánta aleatoriedad hay
> en la selección del siguiente token — cerca de 0 es determinista y consistente, cerca
> de 1 es creativo e impredecible.

---

## 1) Analogía sencilla

Imagina que estás eligiendo la siguiente palabra en un texto y tienes una ruleta con
todas las palabras posibles, donde las más probables ocupan más espacio.

- **Temperature 0**: la ruleta está fija — siempre cae en el espacio más grande
  (la palabra más probable). Resultado predecible y consistente.
- **Temperature 1**: agitas la ruleta fuerte — las palabras menos probables tienen más
  chance de ganar. Resultado creativo y variado.

No cambias *cuáles* palabras están disponibles, solo cuánto pesa la probabilidad
al elegir.

---

## 2) ¿Qué es realmente?

Temperature es un parámetro (rango 0–1) que modifica la distribución de probabilidades
sobre el vocabulario en cada paso de generación:

| Temperature | Efecto | Uso |
|-------------|--------|-----|
| 0 (o cerca) | Siempre selecciona el token más probable → output determinista | Extracción de datos, tareas factuales, JSON estructurado |
| 0.5 | Balance entre consistencia y variedad | Uso general |
| 1 (o cerca) | Tokens menos probables tienen más chance → output creativo/variado | Brainstorming, escritura creativa, chistes, marketing |

---

## 3) ¿Cómo funciona? (mecanismo interno)

En cada paso de generación, el modelo calcula probabilidades para todos los tokens
del vocabulario. Temperature escala esas probabilidades antes de seleccionar:

```
Temperature baja → amplifica diferencias entre probabilidades
                  → el token más probable domina aún más
                  → "gana siempre el favorito"

Temperature alta → aplana las diferencias entre probabilidades
                 → tokens menos probables tienen más chance
                 → "cualquier candidato puede ganar"
```

**Implementación:**

```python
# Tarea factual — temperatura baja
response = client.messages.create(
    model=MODEL,
    max_tokens=500,
    temperature=0.0,         # Determinista
    messages=[{"role": "user", "content": "¿Cuál es la capital de Francia?"}]
)

# Tarea creativa — temperatura alta
response = client.messages.create(
    model=MODEL,
    max_tokens=500,
    temperature=0.9,         # Creativo
    messages=[{"role": "user", "content": "Escribe 5 nombres creativos para una startup de IA"}]
)
```

---

## 4) ¿Cuándo usarlo?

| Tarea | Temperature recomendada |
|-------|------------------------|
| Extracción de datos, JSON, SQL | 0.0 |
| Preguntas factuales | 0.0 – 0.2 |
| Resúmenes, análisis | 0.3 – 0.5 |
| Generación de contenido | 0.5 – 0.7 |
| Brainstorming, creatividad | 0.7 – 1.0 |
| Chistes, marketing creativo | ~1.0 |

---

## 5) Ejemplo práctico mínimo

```python
def extract_entities(text: str) -> str:
    """Extracción determinista — siempre el mismo resultado"""
    return client.messages.create(
        model=MODEL, max_tokens=200, temperature=0.0,
        messages=[{"role": "user", "content": f"Extract all person names from: {text}"}]
    ).content[0].text

def brainstorm_features(product: str) -> str:
    """Brainstorming creativo — variado cada vez"""
    return client.messages.create(
        model=MODEL, max_tokens=500, temperature=0.9,
        messages=[{"role": "user", "content": f"Genera 10 features creativas para: {product}"}]
    ).content[0].text
```

---

## 6) Conexiones con otros conceptos

- `→ requiere:` [[01_fundamentos_api_y_conversaciones]] — el proceso de generación token a token es el contexto donde actúa temperature.
- `→ aplica en:` [[08_controlling_model_output]] — temperature es uno de los mecanismos de control del output.
- `→ aplica en:` [[09_structured_data]] — para JSON/código estructurado siempre usar temperature=0.

---

## 7) Preguntas Feynman

1. ¿Temperature alta *garantiza* outputs diferentes en cada llamada? ¿O solo los hace más *probables*?
2. Estás extrayendo fechas de facturas en producción. ¿Qué temperature usas y por qué?
3. ¿Por qué temperature 0 no produce exactamente el mismo output si ejecutas el mismo request 100 veces en diferentes momentos?

---

## 8) Tarjetas Anki

**Q:** ¿Qué controla exactamente el parámetro `temperature` en la generación de texto?
**A:** La distribución de probabilidades sobre el vocabulario al seleccionar el siguiente token. Temperature 0 = siempre el más probable (determinista). Temperature 1 = distribución más plana, tokens menos probables tienen más chance.

**Q:** ¿Qué temperatura usar para extracción de datos o generación de JSON?
**A:** 0 o muy cercano a 0 — se necesita consistencia y determinismo, no creatividad.

---

## 9) Lo que no es obvio

**Temperature alta no garantiza outputs diferentes — solo los hace más probables.**
Con temperature=1, aún podrías obtener el mismo output dos veces. Y con temperature=0,
en la práctica puede haber pequeñas variaciones por hardware/implementación.

**El default no es 0 — es típicamente 1.**
Si no especificas temperature, Claude usa su default (generalmente 1). Para tareas de
extracción en producción, siempre especifica `temperature=0` explícitamente.

**Temperature no afecta la "inteligencia" del modelo.**
No hace al modelo más o menos capaz. Solo afecta la variabilidad de las respuestas.
Un modelo con temperature=0 puede dar respuestas incorrectas con consistencia perfecta.

---

## Notebooks de práctica

> N/A — aún no hay notebook para esta subsección. Los conceptos de temperatura se
> aplican en los notebooks de evaluación (05x) y prompt engineering (06x).

---

### Registro personal
- Qué conecta con mi trabajo: Es el equivalente del parámetro `seed` en modelos de ML — controla reproducibilidad. En pipelines de datos de Protección donde necesito extracción consistente, temperature=0 es obligatorio.
- Dudas abiertas: ¿Temperature interactúa con top_p o top_k? ¿La API de Claude expone esos parámetros también?
- Siguientes pasos: Ver streaming para mejorar la UX.
