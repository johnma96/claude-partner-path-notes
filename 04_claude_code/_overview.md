---
title: "Overview · Claude Code in Action"
authors: ["John Mario Montoya Zapata"]
date: "28/04/2026"
updated: "10/06/2026"
course: "Claude Code in Action"
status: "completado"
tags: ["claude-code", "cli", "flujo-desarrollo", "hooks", "mcp"]
links:
  - "[[INDEX]]"
---

# Claude Code in Action — Overview

> **¿De qué trata este curso?** Muestra cómo integrar Claude Code en flujos de desarrollo
> reales: configuración avanzada, hooks, integración con MCP, y patrones de uso efectivo
> en proyectos de ingeniería.

## Lectures

| # | Nombre | Nota | Estado |
|---|--------|------|--------|
| 1-2 | What is a Coding Assistant? + Claude Code in Action (demos) | [[04_claude_code/01x_what_is_claude_code/010_que_es_claude_code]] | ✅ borrador |
| 3-13 | Getting Hands On (Context · Changes · Commands · MCP · GitHub · Hooks · SDK) | [[04_claude_code/02x_getting_hands_on/020_getting_hands_on]] | ✅ borrador |

## Conceptos clave del curso

- **Coding assistant = LLM + tool use**: el modelo razona, las herramientas actúan — sin tool use el LLM solo puede hablar del código
- **Loop de tool use**: Claude solicita acción → Claude Code ejecuta → resultado vuelve a Claude → repite hasta tarea completa
- **Extensibilidad vía MCP**: `claude mcp add` conecta cualquier servidor MCP (Playwright, Sentry, Jira, herramientas internas)
- **GitHub Actions**: Claude Code corre en CI/CD con herramientas de GitHub (comentarios, commits, PRs, revisiones de seguridad)
- **Ventaja de seguridad**: búsqueda directa en codebase local, sin indexación externa
- **CLAUDE.md en 3 niveles**: máquina (global) / proyecto (commiteado) / local (personal) — combinación de los tres como contexto permanente
- **Hooks como guardianes automáticos**: pre-tool (puede bloquear, exit 2) y post-tool (feedback) intercalan lógica propia en cada tool call de Claude
- **Comandos personalizados**: `.claude/commands/<nombre>.md` → `/nombre` — automatizan tareas repetitivas con `$arguments`
- **SDK programático**: `@anthropic-ai/claude-agent-sdk` · stream asíncrono `for await` · acceso total por defecto, restringir con `allowedTools`

## Conexiones con otros cursos

- `→ requiere:` [[01_agent_skills/_overview]]
- `→ requiere:` [[02_claude_api/_overview]]
- `→ requiere:` [[03_mcp/_overview]]

---

### Registro personal del curso

- Qué aprendí que no esperaba:
- Cómo conecta con mi trabajo en Protección:
