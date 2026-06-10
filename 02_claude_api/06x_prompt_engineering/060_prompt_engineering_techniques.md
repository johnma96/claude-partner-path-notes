---
title: "Building with the Claude API · Técnicas de Prompt Engineering"
authors: ["John Mario Montoya Zapata"]
date: "19/05/2026"
updated: ""
course: "Building with the Claude API"
module: "Prompt Engineering"
lecture: "Prompt Engineering + Being Clear and Direct + Being Specific + Structure with XML Tags + Providing Examples"
stage: "Intermedio"
status: "borrador"
tags: ["claude-api", "prompt-engineering", "xml-tags", "few-shot", "one-shot", "especificidad", "claridad"]
links:
  - "[[INDEX]]"
  - "[[02_claude_api/_overview]]"
  - "[[05_prompt_evaluation]]"
  - "[[02_system_prompts]]"
---

# Técnicas de Prompt Engineering

> **Resumen Feynman (una frase):** Escribir buenos prompts no es intuición — es un proceso
> de aplicar cuatro técnicas concretas en orden (claridad → especificidad → estructura XML
> → ejemplos) y medir el impacto de cada una con el pipeline de evaluación.

---

## 1) Analogía sencilla

Imagina que le das instrucciones a un contratista para remodelar tu apartamento:

- **Versión vaga:** "Mejora el baño." → El contratista improvisa, el resultado es
  impredecible.
- **Clara y directa:** "Reemplaza los azulejos del baño." → Sabe qué hacer, pero no
  sabe el alcance.
- **Específica:** "Reemplaza los azulejos del baño. Usa azulejos blancos de 30x30 cm,
  instálalos en patrón diagonal, deja 2 mm de separación entre ellos." → Resultado
  predecible y verificable.
- **Con XML para separar contextos:** "Aquí está el plano \<plano\>...\</plano\> y aquí
  los materiales aprobados \<materiales\>...\</materiales\>. Úsalos para planear el
  trabajo." → El contratista entiende exactamente qué es qué.
- **Con ejemplo:** "El resultado debe verse así: \<ejemplo\>foto del baño ideal\</ejemplo\>."
  → Sin ambigüedad posible.

Cada técnica reduce la brecha entre lo que imaginas y lo que Claude produce.

---

## 2) ¿Qué es realmente?

**Prompt engineering = aplicar técnicas sistemáticas para mejorar la calidad y
consistencia del output, medidas con el pipeline de evaluación.**

El flujo es siempre el mismo: escribir prompt → evaluar con pipeline → aplicar técnica
→ re-evaluar → comparar puntajes.

### Las cuatro técnicas, en orden de aplicación

| # | Técnica | Qué controla | Impacto típico |
|---|---------|-------------|---------------|
| 1 | **Claridad y acción directa** | La tarea principal | 2.32 → 3.92 |
| 2 | **Especificidad** (tipo A + tipo B) | El output y el proceso | 3.92 → 7.86 |
| 3 | **XML tags** | La estructura y separación de contextos | Varía |
| 4 | **Ejemplos** (one-shot/multi-shot) | Casos edge y formatos complejos | Varía |

---

## 3) ¿Cómo funciona cada técnica?

### Técnica 1 — Claridad y acción directa

**Regla:** La primera línea es lo más importante. Debe tener un **verbo de acción** seguido
de la tarea exacta y las especificaciones del output.

```
❌ "This prompt is about meal planning for athletes..."
✅ "Generate a one-day meal plan for an athlete that meets their dietary restrictions."
```

**Estructura:** `[Verbo de acción] + [descripción clara de la tarea] + [especificación del output]`

Más ejemplos:
- `"Write three paragraphs about how solar panels work"`
- `"Identify three countries that use geothermal energy and for each include generation stats"`
- `"Extract all AWS service names from the following text"`

---

### Técnica 2 — Especificidad: dos tipos de guidelines

**Tipo A — Atributos del output** → controla *cómo debe ser* el resultado:
```
- Length: 3-5 sentences per section
- Format: Use markdown with headers
- Tone: Technical but accessible
- Structure: Include pros/cons for each option
```

**Tipo B — Pasos del proceso** → controla *cómo Claude debe llegar* al resultado:
```
Steps to follow:
1. First analyze the athlete's physical goal
2. Calculate approximate caloric needs
3. Select foods that meet dietary restrictions
4. Distribute meals across the day
5. Verify nutritional balance
```

**Cuándo usar cada uno:**
- Tipo A: casi siempre — define el formato esperado del output.
- Tipo B: para problemas complejos donde quieres que el modelo considere perspectivas
  adicionales o siga un razonamiento específico.

En prompts profesionales se combinan ambos.

---

### Técnica 3 — XML tags para estructurar contextos

Cuando el prompt incluye contenido externo interpolado (datos de usuario, código, documentos),
los XML tags le dicen al modelo exactamente qué es qué.

```python
# Sin XML tags — Claude puede confundir instrucción con dato
prompt = f"""
Debug the following code and fix any issues you find.
{user_code}
{documentation}
"""

# Con XML tags — límites claros entre instrucción y datos
prompt = f"""
Debug the following code and fix any issues you find.

<my_code>
{user_code}
</my_code>

<docs>
{documentation}
</docs>
"""
```

**Reglas para nombrar tags:**
- Específicos y descriptivos: `<sales_records>` mejor que `<data>`
- Que reflejen el contenido: `<athlete_information>`, `<my_code>`, `<user_query>`
- Consistentes a lo largo del prompt

**Por qué funciona:** Claude fue entrenado con XML en su corpus. Los tags son una señal
semántica fuerte para delimitar secciones — más confiable que separadores de texto como
`---` o líneas en blanco.

---

### Técnica 4 — Ejemplos (one-shot / multi-shot)

Proporcionar ejemplos es la técnica más efectiva para:
- Casos edge difíciles de describir en palabras (sarcasmo, ambigüedad)
- Formatos de output complejos (JSON con estructura específica)
- Calibrar el nivel de detalle esperado

**Estructura con XML:**
```xml
<example>
  <input>¿Cómo configuro un S3 bucket para hosting estático?</input>
  <ideal_output>
    Para configurar S3 como hosting estático:
    1. Habilita "Static website hosting" en Properties
    2. Configura el index document (ej: index.html)
    3. Agrega una bucket policy para acceso público
    El endpoint quedará disponible en: bucket-name.s3-website-region.amazonaws.com
  </ideal_output>
  <reasoning>
    Esta respuesta es ideal porque: da los pasos exactos en orden, incluye
    el ejemplo concreto del index document, y termina con el resultado tangible.
  </reasoning>
</example>
```

**Buenas prácticas:**
- Siempre envuelve los ejemplos en XML para que Claude los distinga del prompt real.
- Incluye el campo `<reasoning>` explicando *por qué* el output es ideal — esto refuerza
  el comportamiento deseado.
- Los mejores ejemplos son los casos con mayor puntaje en el pipeline de evaluación.
- Ubica los ejemplos **después** de las instrucciones principales, no antes.

---

## 4) ¿Cuándo usarlo?

| Situación | Técnica a aplicar |
|-----------|------------------|
| Prompt con score bajo y sin instrucciones claras | Primero: claridad y acción directa |
| Output con formato inconsistente | Tipo A: especificar atributos del output |
| Claude ignora algunos pasos del razonamiento | Tipo B: especificar pasos del proceso |
| Prompt mezcla instrucciones con datos del usuario | XML tags |
| Hay casos edge que el prompt no captura bien | Agregar ejemplos con reasoning |
| Claude produce el formato correcto en algunos casos pero no todos | Multi-shot (varios ejemplos) |

---

## 5) Ejemplo práctico integrado

Evolución de un prompt de análisis de DAGs de Airflow, de peor a mejor:

```python
# V1: Vago (score ~2)
prompt_v1 = "Analyze this Airflow DAG."

# V2: Claro y directo (score ~4)
prompt_v2 = "Review the following Airflow DAG for compliance with best practices."

# V3: Específico con atributos + pasos (score ~7)
prompt_v3 = """
Review the following Airflow DAG for compliance with Protección's engineering standards.

Guidelines:
- Length: Provide 3-5 specific findings, not a generic list
- Format: Group findings by: Critical Issues | Warnings | Suggestions
- Tone: Technical, direct

Steps to follow:
1. Check for hardcoded values (credentials, paths, dates)
2. Verify SLA is defined for the DAG
3. Review task dependencies for circular issues
4. Check retry policies are set
5. Validate schedule_interval uses cron notation, not timedelta
"""

# V4: Con XML para separar el código del DAG (score ~8)
prompt_v4 = f"""
Review the following Airflow DAG for compliance with Protección's engineering standards.

<dag_code>
{dag_source_code}
</dag_code>

<standards>
{internal_standards_doc}
</standards>

Guidelines: ...
Steps: ...
"""

# V5: Con ejemplo de output ideal (score ~9)
prompt_v5 = f"""
Review the following Airflow DAG...

<example>
  <input>DAG with hardcoded password and no SLA</input>
  <ideal_output>
    **Critical Issues**
    - Line 12: Hardcoded password in connection string → move to Airflow Variable or Secret
    - No SLA defined → add sla=timedelta(hours=2) to DAG args

    **Warnings**
    - retry_delay uses timedelta(minutes=5) → acceptable but document the rationale

    **Suggestions**
    - Consider adding email_on_failure=True for production visibility
  </ideal_output>
  <reasoning>Ideal because: specific line references, actionable fixes, grouped correctly</reasoning>
</example>

<dag_code>{dag_source_code}</dag_code>
"""
```

---

## 6) Conexiones con otros conceptos

- `→ requiere:` [[05_prompt_evaluation]] — las mejoras de cada técnica solo son verificables con el pipeline de evaluación. Sin puntaje objetivo, no sabes si mejoraste.
- `→ extiende:` [[02_system_prompts]] — las técnicas aplican tanto al system prompt como al user prompt.
- `→ aplica en:` [[01_agent_skills/03_configuration_and_multi_file_skills]] — la descripción de un skill es un prompt; las mismas técnicas de claridad y especificidad aplican para mejorar el matching semántico.

---

## 7) Preguntas Feynman

1. Tienes un prompt que produce outputs de longitud muy variable — a veces 2 líneas, a veces 20. ¿Qué técnica aplicas primero y qué añades exactamente?
2. ¿Cuál es la diferencia entre Tipo A y Tipo B de guidelines? Da un ejemplo concreto donde necesitas uno pero no el otro.
3. Tienes un prompt que funciona bien en el 80% de casos pero falla consistentemente cuando el usuario hace preguntas con sarcasmo. ¿Qué técnica resuelve esto mejor y cómo la implementas?
4. ¿Por qué se recomienda poner los ejemplos *después* de las instrucciones y no antes?
5. Tu prompt tiene un puntaje de 7.8 en el eval. Decides agregar XML tags. El puntaje sube a 8.1. ¿Fue significativa la mejora? ¿Cuándo tiene más impacto esta técnica?

---

## 8) Tarjetas Anki

**Q:** ¿Cuál es la regla más importante para la primera línea de un prompt?
**A:** Debe comenzar con un **verbo de acción** seguido de la tarea exacta y las especificaciones del output. Es la parte más crítica porque establece el marco de toda la respuesta.

**Q:** ¿Cuál es la diferencia entre guidelines Tipo A y Tipo B?
**A:** **Tipo A (Atributos)**: controla *cómo es* el output (formato, longitud, tono, estructura). **Tipo B (Pasos)**: controla *cómo Claude llega* al output (proceso de razonamiento). Tipo A casi siempre; Tipo B para problemas complejos con múltiples perspectivas.

**Q:** ¿Por qué usar XML tags en vez de separadores de texto como `---`?
**A:** Claude fue entrenado con XML en su corpus — los tags son señales semánticas más fuertes y confiables que separadores de texto para delimitar secciones de contenido externo interpolado.

**Q:** ¿Qué información debe incluir un buen ejemplo en un prompt?
**A:** `<input>` (el caso), `<ideal_output>` (el resultado esperado), y `<reasoning>` (por qué ese output es ideal). El reasoning refuerza el comportamiento deseado más allá del ejemplo mismo.

**Q:** ¿En qué tipo de problema los ejemplos (one-shot/multi-shot) tienen más impacto?
**A:** Casos edge difíciles de describir en palabras (sarcasmo, ambigüedad), formatos de output muy específicos, y cuando se necesita calibrar el nivel de detalle esperado.

---

## 9) Lo que no es obvio

**El orden de aplicación importa.**
Agregar ejemplos a un prompt vago no resuelve la vaguedad — el modelo seguirá sin saber
qué hacer. La secuencia correcta es: claridad primero, luego especificidad, luego
estructura, luego ejemplos. Cada técnica construye sobre la anterior.

**Tipo B (pasos) puede empeorar el resultado si el modelo ya razona bien.**
Si el modelo naturalmente considera todos los ángulos relevantes, imponer pasos rígidos
puede limitar su razonamiento. Usa Tipo B solo cuando el modelo omite sistemáticamente
perspectivas importantes que quieres que considere.

**Los ejemplos negativos también son válidos.**
Puedes incluir `<bad_example>` que muestre qué NO hacer. A veces es más fácil describir
el error que describir el ideal, especialmente para formatos muy específicos.

**El puntaje del eval es relativo al grader, no absoluto.**
Un 7.8 con un grader exigente puede ser mejor que un 9.2 con uno permisivo. Lo que
importa es la mejora relativa entre versiones del prompt con el mismo grader.

**Los XML tags no son magia — los nombres malos los anulan.**
Un tag `<data>` o `<content>` no aporta más que texto plano. El valor está en la
semántica del nombre: `<customer_complaint>`, `<reference_schema>`, `<dag_code>`.

---

## Notebooks de práctica

| Notebook | Qué cubre |
|----------|----------|
| [061_prompting.ipynb](061_prompting.ipynb) | Prompt de meal planning · aplicación secuencial de las 4 técnicas · evaluación con scores por versión |

**Datos generados:**
- `dataset.json` — casos de prueba de atletas con height/weight/goal/dietary
- `output.json` — respuestas del modelo por versión del prompt
- `output.html` — reporte visual HTML con scores y comparativas

---

### Registro personal
- Qué conecta con mi trabajo: El patrón de XML tags para separar instrucción de datos
  es exactamente lo que hago en BigQuery cuando separo el SQL de los comentarios de
  documentación. La misma necesidad de delimitar "esto es código" vs "esto es contexto".
  Para los prompts de análisis de DAGs en Protección, Tipo B (pasos) tiene mucho valor
  porque quiero que Claude siga un checklist específico de nuestros estándares internos.
- Dudas abiertas: ¿Hay un punto de rendimientos decrecientes con los ejemplos?
  ¿5 ejemplos siempre mejor que 3, o puede haber demasiados?
- Siguientes pasos: Aplicar estas técnicas al prompt `airflow-dag-review` y medir con
  el pipeline de eval.
