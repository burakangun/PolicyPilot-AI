from typing import List, Tuple
from sentence_transformers import CrossEncoder

_reranker_model = None

def get_reranker() -> CrossEncoder:
    global _reranker_model
    if _reranker_model is None:
        _reranker_model = CrossEncoder("BAAI/bge-reranker-base")
    return _reranker_model


def rerank_chunks(query: str, chunks: List[str], top_k: int = 3) -> List[str]:
    """   
    Args:
        query:  Kullanıcının sorusu.
        chunks: ChromaDB'den gelen ham chunk listesi.
        top_k:  LLM'e gönderilecek en iyi chunk sayısı.
    
    Returns:
        Yeniden sıralanmış, en alakalı chunk listesi.
    """
    if not chunks:
        return []
    
    reranker = get_reranker()
    
    pairs: List[Tuple[str, str]] = [(query, chunk) for chunk in chunks]
    scores = reranker.predict(pairs)
    
    scored_chunks = sorted(zip(scores, chunks), key=lambda x: x[0], reverse=True)
    
    return [chunk for _, chunk in scored_chunks[:top_k]]
