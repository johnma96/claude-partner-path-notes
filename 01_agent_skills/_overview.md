---
title: "Overview · Introduction to Agent Skills"
authors: ["John Mario Montoya Zapata"]
date: "28/04/2026"
course: "Introduction to Agent Skills"
status: "completado"
tags: ["agent-skills", "claude-code", "skills"]
links:
  - "[[INDEX]]"
---

# Introduction to Agent Skills — Overview

> **¿De qué trata este curso?** Introduce el concepto de Agent Skills en Claude Code:
> instrucciones markdown reutilizables que Claude aplica automáticamente según el contexto
> de la tarea, sin necesidad de repetir prompts manualmente.

## Lectures

| # | Nombre | Nota | Estado |
|---|--------|------|--------|
| 1 | What are Skills | [[01_que_son_skills]] | ✅ borrador |
| 2 | Creating Your First Skill | [[02_creating_your_first_skill]] | ✅ borrador |
| 3 | Configuration and Multi-file Skills | [[03_configuration_and_multi_file_skills]] | ✅ borrador |
| 4 | Skills vs Other Claude Code Features | [[04_skills_vs_other_features]] | ✅ borrador |
| 5 | Sharing Skills | [[05_sharing_skills]] | ✅ borrador |
| 6 | Troubleshooting Skills | [[06_troubleshooting_skills]] | ✅ borrador |

## Conceptos clave del curso

- **Skill**: archivo `SKILL.md` con frontmatter `name` + `description` que Claude usa para activación automática.
- **Lazy loading semántico**: Claude carga solo `name + description`; el cuerpo completo se lee solo si hay match.
- **Skills personales** (`~/.claude/skills/`) vs. **skills de proyecto** (`.claude/skills/` en el repo).
- **Activación automática** vs. slash commands (explícitos) vs. CLAUDE.md (siempre en contexto).
- **Estructura obligatoria**: carpeta con nombre del skill + `SKILL.md` con frontmatter `name` + `description`.
- **Jerarquía de prioridad**: Enterprise > Personal > Project > Plugins.
- **Restart requerido** tras crear/editar/eliminar un skill (el índice se construye en startup).
- **Confirmation step**: Claude pide aprobación antes de cargar el cuerpo completo del skill.
- **`allowed-tools`** (lista blanca): restringe herramientas disponibles cuando el skill está activo — útil para workflows de solo lectura o seguridad.
- **`model`** (opcional): fija el modelo de Claude para ese skill específico.
- **Progressive disclosure**: `SKILL.md` < 500 líneas; material extenso en `references/`; scripts se ejecutan (no se leen) para no saturar el contexto.
- **Estructura multi-archivo**: `scripts/`, `references/`, `assets/` como carpetas de soporte.
- **Distribución**: repo commit (`.claude/skills/`) → Plugin → Enterprise managed settings (jerarquía creciente de autoridad).
- **Subagents + skills**: los subagents NO heredan skills automáticamente; deben declararse en el campo `skills:` del frontmatter del agente custom.
- **Built-in agents** (Explorer, Plan, Verify) no pueden usar skills — solo custom agents en `.claude/agents/`.

## Conexiones con otros cursos

- `→ alimenta:` [[04_claude_code/_overview]]
- `→ requiere:` conocimiento básico de Claude Code CLI

---

### Registro personal del curso

- Qué aprendí que no esperaba:
- Cómo conecta con mi trabajo en Protección:
