# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Install dependencies (run once or after pyproject.toml changes)
uv pip install -e .

# Start the MCP server
uv run main.py

# Run all tests
uv run pytest

# Run a single test file
uv run pytest tests/test_document.py

# Run a single test by name
uv run pytest tests/test_document.py::TestBinaryDocumentToMarkdown::test_binary_document_to_markdown_with_pdf
```

## Architecture

This is an MCP (Model Context Protocol) server built with **FastMCP**. The server exposes Python functions as tools that AI assistants can call.

**Entry point**: `main.py` — creates the FastMCP instance, registers tools, and starts the server.

**Tools** live in `tools/` as plain Python functions. They are registered in `main.py` with:

```python
mcp.tool()(my_function)
```

**Tests** live in `tests/` with real document fixtures in `tests/fixtures/` (`.docx`, `.pdf`).

## Defining MCP Tools

Tools are Python functions in `tools/`. Each tool must follow this pattern:

```python
from pydantic import Field

def my_tool(
    param1: str = Field(description="Detailed description of this parameter"),
    param2: int = Field(description="Explain what this parameter does"),
) -> ReturnType:
    """One-line summary of what the tool does.

    Detailed explanation of functionality.

    When to use:
    - Use case 1
    - Use case 2

    When NOT to use:
    - Anti-pattern 1

    Examples:
    >>> my_tool("foo", 42)
    "expected output"
    """
```

Key rules:
- Use `pydantic.Field` for every parameter — the `description` becomes the tool's parameter schema exposed to the AI.
- Docstrings must include: one-line summary, detailed explanation, when to use (and not use), and usage examples with expected output.
- After defining a tool, register it in `main.py` with `mcp.tool()(my_function)`.
