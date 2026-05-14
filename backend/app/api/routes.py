from pathlib import Path
from fastapi import APIRouter, HTTPException
from app.api.schemas import QueryRequest, QueryResponse
from app.rag.vector_store import VectorStore

router = APIRouter(prefix="/api", tags=["PolicyPilot AI"])

PROJECT_ROOT = Path(__file__).resolve().parents[3]
RAW_DOCS_DIR = PROJECT_ROOT / "data" / "raw_docs"
CHROMA_DB_DIR = PROJECT_ROOT / "backend" / "chroma_db"

# Initialize vector store
try:
    vector_store = VectorStore(
        persist_directory=str(CHROMA_DB_DIR), 
        collection_name="policy_collection"
    )
except Exception as e:
    print(f"Warning: Failed to initialize VectorStore. Error: {e}")
    vector_store = None


@router.get("/health")
def health_check():
    return {
        "status": "ok", 
        "vector_store": "initialized" if vector_store else "not_initialized"
    }


@router.get("/documents")
def list_documents():
    documents = sorted([path.name for path in RAW_DOCS_DIR.glob("*.md")])
    return {
        "count": len(documents),
        "documents": documents
    }


@router.post("/query", response_model=QueryResponse)
def query_rag(request: QueryRequest):
    """
    Search the ChromaDB vector store for relevant chunks based on the query.
    """
    if not vector_store:
        raise HTTPException(status_code=500, detail="Vector store is not initialized.")
        
    results = vector_store.search(query=request.query, n_results=request.n_results)
    
    # Format results
    formatted_results = []
    if results and results.get('documents') and len(results['documents'][0]) > 0:
        for i in range(len(results['documents'][0])):
            match_content = results['documents'][0][i]
            metadata = results['metadatas'][0][i]
            
            formatted_results.append({
                "content": match_content,
                "metadata": metadata,
                "distance": results['distances'][0][i] if 'distances' in results and results['distances'] else None
            })
            
    return QueryResponse(query=request.query, results=formatted_results)