from io import BytesIO
from pathlib import Path

from markitdown import MarkItDown, StreamInfo
from pydantic import Field

_SUPPORTED_EXTENSIONS = {"docx", "pdf"}


def binary_document_to_markdown(binary_data: bytes, file_type: str) -> str:
    """Converts binary document data to markdown-formatted text."""
    md = MarkItDown()
    file_obj = BytesIO(binary_data)
    stream_info = StreamInfo(extension=file_type)
    result = md.convert(file_obj, stream_info=stream_info)
    return result.text_content


def document_to_markdown(
    file_path: str = Field(description="Absolute or relative path to a .docx or .pdf file"),
) -> str:
    """Convert a Word (.docx) or PDF file to markdown-formatted text.

    Reads a document from disk and converts its content to markdown,
    preserving headings, lists, and basic text formatting.

    When to use:
    - When you need to extract readable text from a .docx or .pdf file
    - When you want to process or search document content as plain text

    When NOT to use:
    - For file types other than .docx and .pdf
    - When pixel-perfect layout or embedded images must be preserved

    Examples:
    >>> document_to_markdown("/path/to/report.pdf")
    "# Report Title\\n\\nSome content..."
    >>> document_to_markdown("/path/to/notes.docx")
    "# Notes\\n\\n- Item 1\\n- Item 2"
    """
    path = Path(file_path)
    extension = path.suffix.lower().lstrip(".")
    if extension not in _SUPPORTED_EXTENSIONS:
        raise ValueError(
            f"Unsupported file type '.{extension}'. Supported types: {sorted(_SUPPORTED_EXTENSIONS)}"
        )
    return binary_document_to_markdown(path.read_bytes(), extension)
