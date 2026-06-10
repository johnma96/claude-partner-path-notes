---
name: session-recap
description: Genera el resumen de cierre de una jornada de estudio en la ruta Claude
             Partner Network. Úsalo cuando el usuario diga "haz un recuento", "finalicemos
             la jornada", "resumen de lo visto", "qué aprendimos hoy", "cierra la sesión",
             "highlights de la sesión", o pida resumir las lectures vistas y actualizar
             el INDEX.md.
---

## Comportamiento esperado

Cuando este skill se activa, debes:

### 1. Identificar el alcance de la sesión
Lee el INDEX.md para determinar qué notas se crearon o modificaron en la sesión actual.
Compáralas con el estado anterior implícito en la conversación.

### 2. Generar el recuento estructurado

Presenta siempre en este orden:

**a) Arco de la sesión**
Una o dos frases que describan la unidad conceptual que conecta todo lo visto. No es
una lista — es la idea que lo une.

**b) Tabla de lectures cubiertas**
| # | Lecture | Lo que agrega al conocimiento anterior |
|---|---------|----------------------------------------|

**c) Los N insights más valiosos**
N = número de lectures cubiertas, mínimo 3, máximo 7. Para cada insight:
- Una frase en negrita que lo nombre
- Una o dos frases que expliquen por qué importa o qué lo hace no obvio
- Si conecta con el stack de Protección (GCP, BigQuery, Airflow, Vertex AI, GKE,
  Python, MLOps, Docker), señalarlo explícitamente

**d) Dudas abiertas consolidadas**
Lista las dudas que quedaron abiertas en las secciones "Registro personal" de las notas
de la sesión. Si varias apuntan a lo mismo, agrúpalas.

**e) Siguientes pasos sugeridos**
Máximo 3. Priorizados por valor de aplicación en Protección.

### 3. Actualizar INDEX.md

Después de presentar el recuento, actualiza el INDEX.md:

- Marcar lectures como ✅ si no lo estaban
- Actualizar el contador de "Lectures completadas" en la tabla de progreso general
- Si se completó un curso entero, marcar estado como ✅ Completado y añadir fecha
- Actualizar la sección "Conceptos clave por primitiva" con los conceptos nuevos,
  cada uno con wikilink a la nota correspondiente
- Actualizar la sección "Conexión con trabajo en Protección S.A." con las aplicaciones
  concretas identificadas en las notas de la sesión (campo "Siguientes pasos" y
  "Registro personal" de cada nota)
- Actualizar campo "Última actualización" con la fecha actual (formato DD/MM/AAAA)

### 4. Actualizar _overview.md del curso si aplica

Si se completaron lectures de un solo curso, actualiza el `_overview.md` correspondiente:
- Añadir filas a la tabla de lectures si faltan
- Añadir conceptos clave nuevos a la sección "Conceptos clave del curso"
- Si el curso quedó completo, cambiar `status: "en progreso"` a `status: "completado"`

## Tono y formato

- Español colombiano
- Directo — no hay que calentarse con introducción
- El recuento va primero, las actualizaciones de archivos después
- No repetir información que ya está en las notas — sintetizar, no transcribir
- Si una conexión con Protección no es genuina, no forzarla
