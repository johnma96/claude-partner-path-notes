# Claude Partner Network — Study Notes

> Personal study notes from the **Anthropic Claude Partner Network Learning Path**.
>
> Official program: [https://anthropic.skilljar.com/page/claude-partner-network-learning-path](https://anthropic.skilljar.com/page/claude-partner-network-learning-path)

## About this repository

This repo contains structured, in-depth study notes built while completing the Claude Partner Network certification path offered by Anthropic. Notes follow the **Feynman technique** — every concept is explained with an analogy before the technical detail, making knowledge durable and transferable.

Notes are written in **Spanish (Colombian)** as a personal learning choice. Code snippets and filenames are in English.

## Course structure

| # | Course | Status | Notes |
|---|--------|--------|-------|
| 01 | Introduction to Agent Skills | ✅ Complete | Skills in Claude Code: reusable markdown instructions |
| 02 | Building with the Claude API | 🟡 In progress | Messages, tools, streaming, RAG, MCP, and more |
| 03 | Introduction to Model Context Protocol | ⬜ Pending | Building MCP servers and clients in Python |
| 04 | Claude Code in Action | ⬜ Pending | Integrating Claude Code into real development workflows |

## Repository structure

```
📁 /
├── CLAUDE.md                        ← Claude Code instructions for this project
├── INDEX.md                         ← Live knowledge map (maintained by Claude)
│
├── 📁 01_agent_skills/              ← Course 1: Introduction to Agent Skills
│   ├── _overview.md
│   └── [lecture].md
│
├── 📁 02_claude_api/                ← Course 2: Building with the Claude API
│   ├── _overview.md
│   ├── 01x_api_fundamentals/
│   ├── 02x_system_prompts/
│   ├── 03x_temperature/
│   ├── 04x_streaming_and_output/
│   ├── 05x_prompt_evaluation/
│   ├── 06x_prompt_engineering/
│   ├── 07x_tool_use/
│   ├── 08x_rag/
│   ├── 09x_features_claude/
│   └── 010x_mcp/
│
├── 📁 03_mcp/                       ← Course 3: Introduction to MCP
├── 📁 04_claude_code/               ← Course 4: Claude Code in Action
│
└── 📁 _comparativas/                ← Cross-course synthesis notes
```

## Note format

Each lecture note follows a consistent Feynman-inspired template:

1. **Plain-language analogy** — the concept explained without jargon
2. **Technical definition** — precise definition after establishing the analogy
3. **Internal mechanism** — flow, architecture, or logic (with Mermaid diagrams)
4. **When to use it** — concrete use cases, and when not to
5. **Minimal working example** — shortest code that illustrates the concept
6. **Cross-references** — explicit connections to other notes (`→ extends`, `→ requires`, `→ contrasts`, `→ applies in`)
7. **Feynman questions** — 3–5 questions answerable only with real understanding
8. **Anki cards** — ready-to-import flashcard pairs
9. **Non-obvious pitfalls** — traps and misconceptions that often go unnoticed

## Knowledge index

See [INDEX.md](INDEX.md) for the full concept map, cross-course connections, and a transversal index organized by topic rather than by course.

## Tools used

- **Claude Code** — AI coding assistant used throughout the learning process
- **Obsidian** — note navigation via `[[wikilinks]]` and graph view
- **Jupyter Notebooks** — hands-on practice alongside each lecture section
- **uv** — Python package and project manager for the MCP CLI project

## Setup (for hands-on notebooks)

```bash
# Clone the repo
git clone https://github.com/<your-username>/claude-partner-network-notes.git
cd claude-partner-network-notes

# Create a virtual environment (Python 3.10+)
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies for the MCP project
cd 02_claude_api/010x_mcp/cli_project
uv sync
```

Copy `.env.example` to `.env` and add your own API keys — never commit real keys.

## License

Notes and personal content: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — free to use with attribution.
Code snippets in notebooks: MIT License.
