---
title: "Overview · Introduction to Model Context Protocol"
authors: ["John Mario Montoya Zapata"]
date: "28/04/2026"
updated: "10/06/2026"
course: "Introduction to Model Context Protocol"
status: "cubierto en Curso 02"
tags: ["mcp", "tools", "resources", "prompts", "protocolo"]
links:
  - "[[INDEX]]"
  - "[[02_claude_api/_overview]]"
  - "[[02_claude_api/010x_mcp/100_mcp]]"
---

# Introduction to Model Context Protocol — Overview

> **Veredicto:** El contenido de este curso es idéntico a la sección MCP del Curso 02
> (lectures 46–55 de *Building with the Claude API*). No se crean notas duplicadas.
> Todo el material está en [[02_claude_api/010x_mcp/100_mcp]].

---

## Solapamiento con Curso 02

Las siguientes lectures de este curso tienen correspondencia exacta con notas ya existentes:

| Lecture del Curso 03 | Cubierto en |
|---|---|
| Introducing MCP | [[02_claude_api/010x_mcp/100_mcp]] §2 |
| MCP Clients | [[02_claude_api/010x_mcp/100_mcp]] §3.2 |
| Project Setup | [[02_claude_api/010x_mcp/100_mcp]] §5 |
| Defining Tools with MCP | [[02_claude_api/010x_mcp/100_mcp]] §3.1 |
| The Server Inspector | [[02_claude_api/010x_mcp/100_mcp]] §3.5 |
| Implementing a Client | [[02_claude_api/010x_mcp/100_mcp]] §3.2 |
| Defining Resources | [[02_claude_api/010x_mcp/100_mcp]] §3.3 |
| Accessing Resources | [[02_claude_api/010x_mcp/100_mcp]] §3.3 |
| Defining Prompts | [[02_claude_api/010x_mcp/100_mcp]] §3.4 |
| Prompts in the Client | [[02_claude_api/010x_mcp/100_mcp]] §3.4 |

---

## Único aporte nuevo: modelo de control de primitivas

La nota de cierre "MCP Review" del Curso 03 introduce un framing que no aparece
explícitamente en el Curso 02 — las tres primitivas clasificadas por **quién decide
cuándo invocarlas**:

| Primitiva | Controlada por | Propósito |
|---|---|---|
| **Tools** | El modelo (Claude) | Añadir capacidades a Claude — Claude decide cuándo llamarlas |
| **Resources** | La aplicación | Obtener datos para UI o para aumentar prompts — el código decide cuándo pedirlos |
| **Prompts** | El usuario | Flujos predefinidos activados por el usuario (botones, slash commands) |

Regla de diseño: ¿Necesitas darle capacidades a Claude? → implementa **tools**.
¿Necesitas datos en tu app? → usa **resources**. ¿Necesitas un flujo para el usuario? → crea **prompts**.

---

## Conexiones con otros cursos

- `→ extiende:` [[02_claude_api/_overview]] — el contenido de este curso está íntegramente cubierto allí
- `→ alimenta:` [[04_claude_code/_overview]]

---

### Registro personal del curso

- Decisión: No duplicar notas. El grafo de conocimiento gana claridad con un único nodo MCP.
- Aporte real del Curso 03: el modelo mental "quién controla qué" para diseñar primitivas MCP.
