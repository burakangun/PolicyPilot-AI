import os
from typing import List
import chromadb
from chromadb.utils import embedding_functions
from app.rag.schemas import DocumentChunk

class VectorStore:
    """
    A class to handle the storage and retrieval of DocumentChunks using ChromaDB
    and SentenceTransformers for embeddings.
    """
    def __init__(self, persist_directory: str = "./chroma_db", collection_name: str = "policy_documents"):
        self.client = chromadb.PersistentClient(path=persist_directory)
        
        # Turkce destegi icin Multilingual model sart. Aksi halde aramalar sacmalar.
        self.embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="paraphrase-multilingual-MiniLM-L12-v2")
        
        self.collection = self.client.get_or_create_collection(
            name=collection_name,
            embedding_function=self.embedding_function
        )

    def add_chunks(self, chunks: List[DocumentChunk]):
        """
        Takes a list of DocumentChunks, calculates their embeddings, 
        and stores them in the ChromaDB collection.
        """
        if not chunks:
            return

        documents = []
        metadatas = []
        ids = []

        for chunk in chunks:
            documents.append(chunk.content)
            clean_metadata = {k: v for k, v in chunk.metadata.items() if v is not None}
            clean_metadata["document_name"] = chunk.document_name
            metadatas.append(clean_metadata)
            ids.append(chunk.chunk_id)

        self.collection.upsert(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )

    def search(self, query: str, n_results: int = 3):
        """
        Searches the database for chunks most similar to the query.
        """
        results = self.collection.query(
            query_texts=[query],
            n_results=n_results
        )
        return results
