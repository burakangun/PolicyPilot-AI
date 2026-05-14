from pydantic import BaseModel
from typing import List, Dict, Any

class QueryRequest(BaseModel):
    query: str
    n_results: int = 3

class QueryResponse(BaseModel):
    query: str
    answer: str
    results: List[Dict[str, Any]]
