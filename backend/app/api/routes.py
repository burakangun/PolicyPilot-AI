from pathlib import Path
from fastapi import APIRouter, HTTPException
from app.api.schemas import QueryRequest, QueryResponse
from app.rag.vector_store import VectorStore
from app.rag.generator import LLMGenerator
from app.rag.router import detect_intent, CHITCHAT_RESPONSE
from app.rag.reranker import rerank_chunks

router = APIRouter(prefix="/api", tags=["PolicyPilot AI"])

PROJECT_ROOT = Path(__file__).resolve().parents[3]
RAW_DOCS_DIR = PROJECT_ROOT / "data" / "raw_docs"
CHROMA_DB_DIR = PROJECT_ROOT / "backend" / "chroma_db"

# Initialize vector store and LLM Generator
try:
    vector_store = VectorStore(
        persist_directory=str(CHROMA_DB_DIR), 
        collection_name="policy_collection"
    )
except Exception as e:
    print(f"Warning: Failed to initialize VectorStore. Error: {e}")
    vector_store = None

try:
    llm_generator = LLMGenerator()
except Exception as e:
    print(f"Warning: Failed to initialize LLMGenerator. Error: {e}")
    llm_generator = None


@router.get("/health")
def health_check():
    return {
        "status": "ok", 
        "vector_store": "initialized" if vector_store else "not_initialized",
        "llm_generator": "initialized" if llm_generator else "not_initialized"
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
    Aşama 1: Semantic Router — gelen mesajın niyetini tespit eder.
    Aşama 2: Eğer POLICY_QUERY ise ChromaDB'de arama yapar.
    Aşama 3: Bulunan chunk'ları LLM'e gönderip cevap üretir.
    """
    # --- AŞAMA 1: SEMANTIC ROUTER ---
    # Her soru için veritabanını ve LLM'i çalıştırmak israf.
    # Önce niyeti tespit et; sohbet mesajlarını anında yanıtla.
    intent = detect_intent(request.query)
    
    if intent == "CHITCHAT":
        return QueryResponse(
            query=request.query,
            answer=CHITCHAT_RESPONSE,
            results=[]
        )

    # --- AŞAMA 2: RAG PIPELINE (Sadece POLICY_QUERY için) ---
    if not vector_store:
        raise HTTPException(status_code=500, detail="Vector store is not initialized.")
    if not llm_generator:
        raise HTTPException(status_code=500, detail="LLM Generator is not initialized.")

    # Daha geniş bir aday havuzu çek (10 chunk), sonra re-ranker ile en iyi 3'e indir.
    # Bu tekniğe sektörde "Retrieve & Re-rank" denir.
    candidate_count = request.n_results * 3
    results = vector_store.search(query=request.query, n_results=candidate_count)

    formatted_results = []
    raw_chunks = []

    if results and results.get('documents') and len(results['documents'][0]) > 0:
        raw_chunks = results['documents'][0]
        for i in range(len(results['documents'][0])):
            formatted_results.append({
                "content": results['documents'][0][i],
                "metadata": results['metadatas'][0][i],
                "distance": results['distances'][0][i] if 'distances' in results and results['distances'] else None
            })

    # --- AŞAMA 2.5: RE-RANKING ---
    # Cross-Encoder, soruyu ve her chunk'ı birlikte değerlendirip
    # en alakalı olanları seçer. LLM'e sadece bunlar gider.
    context_chunks = rerank_chunks(query=request.query, chunks=raw_chunks, top_k=request.n_results)

    # --- AŞAMA 3: LLM GENERATION ---
    answer = llm_generator.generate_answer(query=request.query, context_chunks=context_chunks)

    return QueryResponse(
        query=request.query,
        answer=answer,
        results=formatted_results
    )