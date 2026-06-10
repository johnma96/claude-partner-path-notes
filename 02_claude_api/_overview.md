---
title: "Overview · Building with the Claude API"
authors: ["John Mario Montoya Zapata"]
date: "28/04/2026"
updated: "10/06/2026"
course: "Building with the Claude API"
status: "completado"
tags: ["claude-api", "anthropic", "sdk", "mensajes", "herramientas"]
links:
  - "[[INDEX]]"
---

# Building with the Claude API — Overview

> **¿De qué trata este curso?** Cubre el espectro completo de integración con los modelos
> Anthropic vía API: estructura de mensajes, uso de herramientas (tool use), streaming,
> manejo de contexto, prompt caching y más.

## Lectures

| # | Nombre | Nota | Estado |
|---|--------|------|--------|
| 1-4 | Modelos · Flujo API · Request · Multi-turn | [[02_claude_api/01x_api_fundamentals/010_fundamentos_api_y_conversaciones]] | ✅ borrador |
| 5 | System Prompts | [[02_claude_api/02x_system_prompts/020_system_prompts]] | ✅ borrador |
| 6 | Temperature | [[02_claude_api/03x_temperature/030_temperature]] | ✅ borrador |
| 7-9 | Response Streaming + Controlling Output | [[02_claude_api/04x_streaming_and_output/040_response_streaming]] | ✅ borrador |
| 10-15 | Prompt Evaluation (subsección completa) | [[02_claude_api/05x_prompt_evaluation/050_prompt_evaluation]] | ✅ borrador |
| 16-20 | Prompt Engineering Techniques | [[02_claude_api/06x_prompt_engineering/060_prompt_engineering_techniques]] | ✅ borrador |
| 21-30 | Tool Use (herramientas, batch, structured data, streaming) | [[02_claude_api/07x_tool_use/070_tool_use]] | ✅ borrador |
| 31-39 | RAG y Agentic Search | [[02_claude_api/08x_rag/080_rag_and_agentic_search]] | ✅ borrador |
| 40-45 | Features de Claude (Thinking, Vision, Citations, Caching, Code Execution) | [[02_claude_api/09x_features_claude/090_features_claude]] | ✅ borrador |
| 46-55 | Model Context Protocol (FastMCP · Tools · Resources · Prompts · MCPClient · Inspector) | [[02_claude_api/010x_mcp/100_mcp]] | ✅ borrador |
| 56-63 | Anthropic Apps: Claude Code in Action + Computer Use | [[02_claude_api/011x_anthropic_apps/110_anthropic_apps]] | ✅ borrador |
| 64-70 | Agents and Workflows (Eval-Optimizer · Parallelization · Chaining · Routing · Agents · Environment Inspection) | [[02_claude_api/012x_agents_and_workflows/120_agents_and_workflows]] | ✅ borrador |

## Conceptos clave del curso

- **Flujo de 5 pasos** + proceso interno (tokenización → embedding → contextualización → generación)
- **API stateless**: el developer mantiene y envía el historial completo en cada request
- **Parámetros clave**: `model`, `max_tokens`, `messages`, `system`, `temperature`
- **Streaming**: chunks vía `text_stream`; mensaje completo vía `get_final_message()`
- **Prompt Evaluation**: pipeline dataset → `run_prompt` → grader → score promedio → iterar
- **Tipos de grader**: code (sintaxis), model (semántica vía LLM), human (máxima precisión)
- **Prompt engineering**: claridad (verbo de acción) → Tipo A (atributos) → Tipo B (pasos) → XML tags → ejemplos one-shot/multi-shot
- **Tool use**: schema JSON + loop `run_conversation` + dispatcher `run_tool` + `tool_result` de vuelta como mensaje de usuario
- **Tools built-in**: Web Search y Code Execution (lado servidor, sin implementación) · Text Editor y Computer Use (lado cliente, tú implementas)
- **RAG**: chunking → embeddings Voyage AI → VectorIndex + BM25 → RRF → reranking LLM → contextual retrieval
- **Prompt Caching**: `cache_control` en system prompt / tools · TTL 1h · mínimo 1024 tokens · máx 4 breakpoints
- **Extended Thinking**: thinking budget · thinking block + firma criptográfica · usar solo después de optimizar prompts
- **Vision/PDF**: bloques `image` y `document` en el content · prompting cuidadoso para imágenes
- **Citations**: `citation_page_location` (PDF) y `citation_char_location` (texto) · transparencia sobre fuentes
- **Code Execution + Files API**: Docker aislado sin red · I/O solo vía Files API · tool del lado del servidor
- **MCP**: protocolo que delega definición y ejecución de herramientas a un servidor especializado — elimina escribir schemas a mano
- **FastMCP**: `@mcp.tool` / `@mcp.resource` / `@mcp.prompt` — schemas generados automáticamente desde Python con Pydantic `Field()`
- **MCPClient**: wrapper de `ClientSession` con `AsyncExitStack`; métodos: `list_tools()`, `call_tool()`, `list_prompts()`, `get_prompt()`, `read_resource()`
- **Transport stdio**: servidor lanzado como subproceso; comunicación por stdin/stdout — más común en desarrollo
- **Tools vs Resources**: tools = reactivo (Claude las invoca); resources = proactivo (cliente solicita por URI directa o templada)
- **Prompts MCP**: retornan `list[base.Message]` listos para Claude — slash commands pre-evaluados por el autor del servidor
- **Claude Code**: agente de desarrollo en terminal — `CLAUDE.md` como memoria de proyecto, tres tipos de memoria (Project/Local/User), cliente MCP nativo
- **Git work trees**: copias físicas del proyecto en directorios separados para paralelizar instancias de Claude Code sin conflictos
- **Debugging automatizado**: GitHub Actions + CloudWatch + Claude Code → PR con fixes sin intervención manual
- **Computer Use**: loop screenshot → Claude → acción (clic/tecla) sobre Docker container — mismo mecanismo de tool use, schema `computer_20250124`
- **Workflows vs Agentes**: workflow cuando los pasos son conocidos (alta confiabilidad); agente cuando son desconocidos (flexibilidad); preferir workflow por defecto
- **Patrones de workflow**: Evaluador-Optimizador (produce→evalúa→loop) · Paralelización (fan-out→agregador) · Chaining (output_N = input_N+1) · Routing (clasificar→pipeline especializado)
- **Diseño de agentes**: herramientas abstractas > especializadas · Environment Inspection tras cada acción · puede pedir inputs adicionales al usuario

## Conexiones con otros cursos

- `→ alimenta:` [[03_mcp/_overview]]
- `→ alimenta:` [[04_claude_code/_overview]]
- `→ requiere:` [[01_agent_skills/_overview]]

---

### Registro personal del curso

- Qué aprendí que no esperaba: La firma criptográfica en Extended Thinking blocks y la distinción entre tools del lado del servidor vs cliente fue lo más no obvio. También el concepto de Code Execution como sandbox Docker sin red — el I/O forzado por Files API es una decisión de seguridad deliberada.
- Cómo conecta con mi trabajo en Protección: Prompt Caching para system prompts con normativa SFC, Citations para herramientas de consulta jurídica, Code Execution como alternativa a scripts ETL para análisis ad-hoc de datos.
