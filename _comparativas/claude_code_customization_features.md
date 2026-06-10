---
title: "Comparativa · Los 5 mecanismos de personalización de Claude Code"
authors: ["John Mario Montoya Zapata"]
date: "28/04/2026"
updated: ""
type: "comparativa"
stage: "Intermedio"
status: "borrador"
tags: ["skills", "claude-md", "hooks", "subagents", "mcp", "claude-code", "comparativa"]
links:
  - "[[INDEX]]"
  - "[[01_agent_skills/04_skills_vs_other_features]]"
  - "[[03_mcp/_overview]]"
  - "[[04_claude_code/_overview]]"
---

# Los 5 mecanismos de personalización de Claude Code

> **Para qué sirve esta nota:** Referencia rápida para decidir qué mecanismo usar ante
> un nuevo requerimiento. Se actualiza a medida que avanzan los cursos 3 y 4.

---

## Tabla maestra de decisión

| Mecanismo | Cuándo activa | Scope | ¿Modifica contexto? | Caso de uso típico |
|-----------|--------------|-------|--------------------|--------------------|
| **CLAUDE.md** | Siempre, cada conversación | Proyecto / global | Sí — siempre | Invariantes del proyecto, estándares que nunca deben violarse |
| **Skills** | Match semántico con la petición | Personal / proyecto | Sí — on demand | Expertise específico por tarea: PR review, commit format, dag review |
| **Hooks** | Evento del sistema (save, tool call) | Proyecto | No — ejecuta side effects | Lint on save, validaciones pre-commit, formateo automático |
| **Subagents** | Delegación explícita | Contexto aislado | No — contexto propio | Tareas paralelas, trabajo que no debe contaminar la conversación principal |
| **MCP servers** | Herramienta disponible en sesión | Global / proyecto | No — provee capacidades | Conexión a BigQuery, GitHub, Slack, bases de datos externas |

---

## Árbol de decisión

```
¿Necesito que algo aplique en TODA conversación sin excepción?
  └── Sí → CLAUDE.md

¿Necesito conocimiento/instrucciones que apliquen SOLO cuando la tarea lo requiere?
  └── Sí → Skill

¿Necesito que algo ocurra automáticamente ante un EVENTO (save, tool call)?
  └── Sí → Hook

¿Necesito DELEGAR trabajo a un contexto aislado?
  └── Sí → Subagent

¿Necesito conectar Claude con un SISTEMA EXTERNO (BD, API, servicio)?
  └── Sí → MCP server
```

---

## Ejes de comparación clave

### Eje 1: ¿Cuándo activa?

```
Siempre          →  CLAUDE.md
Request-driven   →  Skills
Event-driven     →  Hooks
Delegación       →  Subagents
Disponibilidad   →  MCP servers
```

### Eje 2: ¿Qué hace con el contexto de la conversación?

```
Lo carga siempre       →  CLAUDE.md
Lo enriquece on demand →  Skills
No lo toca             →  Hooks (ejecuta externamente)
Tiene el suyo propio   →  Subagents
Expone herramientas    →  MCP servers
```

### Eje 3: ¿Quién "sabe" que está ocurriendo?

```
Siempre visible para Claude  →  CLAUDE.md
Visible cuando activa        →  Skills (Claude indica que usó el skill)
Puede ser transparente       →  Hooks
Resultado visible            →  Subagents (retornan output)
Transparente como herramienta→  MCP servers
```

---

## Combinaciones naturales

| Escenario | Combinación recomendada |
|-----------|------------------------|
| Revisión de PRs con estándares de equipo | Skill (checklist) + Hook (lint automático on save) |
| Análisis de datos en BigQuery | MCP server (conexión BQ) + Skill (metodología de análisis) |
| Onboarding de nuevo developer | Skill (codebase-onboarding, `allowed-tools: Read`) + CLAUDE.md (invariantes del proyecto) |
| Pipeline de CI automatizado | Hook (validaciones on commit) + Subagent (ejecuta suite de tests en paralelo) |
| Gestión de DAGs de Airflow | Skill (airflow-dag-review) + MCP server (conexión Airflow API) + Hook (lint .py on save) |

---

## Antipatrones frecuentes

| Antipatrón | Problema | Solución |
|------------|----------|----------|
| Todo en CLAUDE.md | Contexto inflado; 80% irrelevante para cada tarea | Mover procedimientos específicos a skills |
| Skills para invariantes | El skill puede no activarse cuando la regla debe aplicarse siempre | Mover invariantes a CLAUDE.md |
| Confundir subagents con skills múltiples | Dos skills no crean paralelismo ni aislamiento | Usar subagent para trabajo delegado |
| MCP como skills "con superpoderes" | Categorías distintas: MCP provee herramientas, skills proveen instrucciones | Usarlos como complemento, no sustitutos |

---

## Estado de notas por mecanismo

| Mecanismo | Nota(s) | Curso | Estado |
|-----------|---------|-------|--------|
| Skills | [[01_que_son_skills]], [[02_creating_your_first_skill]], [[03_configuration_and_multi_file_skills]] | 01 | ✅ borrador |
| CLAUDE.md vs Skills | [[04_skills_vs_other_features]] | 01 | ✅ borrador |
| Hooks | *(pendiente — Curso 4)* | 04 | ⬜ |
| Subagents | *(pendiente — Curso 4)* | 04 | ⬜ |
| MCP servers | *(pendiente — Curso 3)* | 03 | ⬜ |

---

*Esta nota se actualizará a medida que los cursos 3 y 4 profundicen en hooks, subagents y MCP.*
