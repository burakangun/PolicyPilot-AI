from pathlib import Path
from app.rag.schemas import RawDocument


def extract_frontmatter(content: str) -> tuple[dict, str]:
    """
    Extracts the YAML-like metadata section (front matter) from the beginning of the Markdown file.

    Example:
    ---
    title: Privacy Policy
    version: 1.0
    ---
    """
    if not content.startswith("---"):
        return {}, content

    parts = content.split("---", 2)

    if len(parts) < 3:
        return {}, content

    raw_metadata = parts[1].strip()
    body = parts[2].strip()

    metada = {}

    for line in raw_metadata.splitlines():
        if ":" not in line:
            continue
            
        key,value =line.split(":",1)
        metadata[key.strip()] = value.strip()

    return metadata, body


def load_markdown_document(file_path:Path) -> RawDocument:
    content = file_path.read_text(encoding="utf-8")
    metadata, body = extract_frontmatter(content)

    metadata["source_path"] = str(file_path)
    
    return RawDocument(
        document_name=file_path.name,
        content=body,
        metadata=metadata,
    )

def load_documents(raw_docs_dir: Path) -> list[RawDocument]:
    documents = []

    for file_path in sorted(raw_docs_dir.glob("*md")):
        documents.append(load_markdown_document(file_path))

    return documents



