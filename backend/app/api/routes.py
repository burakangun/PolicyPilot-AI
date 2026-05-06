from pathlib import Path
from fastapi import APIRouter

router = APIRouter(prefix="/api", tags=["PolicyPilot AI"])

PROJECT_ROOT = Path(__file__).resolve().parents[3]
RAW_DOCS_DIR = PROJECT_ROOT / "data" / "raw_docs"


@router.get("/health")
def health_check():
    return {"status": "ok"}


@router.get("/documents")
def list_documents():
    documents = sorted([path.name for path in RAW_DOCS_DIR.glob("*.md")])

    return {
        "count": len(documents),
        "documents": documents
    }