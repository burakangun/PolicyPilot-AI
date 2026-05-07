import uuid
from typing import List
from app.rag.schemas import RawDocument, DocumentChunk

class TextSplitter:
    """
    A class that splits large texts into smaller, manageable pieces (chunks)
    for LLMs to process.
    """
    def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 200):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def split_text(self, text: str) -> List[str]:
        """
        Splits the text based on the maximum chunk_size.
        Splits by spaces to avoid cutting words in half.
        """
        words = text.split(" ")
        chunks = []
        current_chunk = []
        current_length = 0

        for word in words:
            # +1 for the space character
            word_length = len(word) + 1 
            
            if current_length + word_length > self.chunk_size and current_chunk:
                # If the chunk is full, add it to the list
                chunks.append(" ".join(current_chunk))
                
                # Overlap Logic:
                # When moving to the next chunk, we take the last few words
                # of the previous chunk. This prevents the loss of context.
                overlap_length = 0
                overlap_chunk = []
                for w in reversed(current_chunk):
                    if overlap_length + len(w) + 1 <= self.chunk_overlap:
                        overlap_chunk.insert(0, w)
                        overlap_length += len(w) + 1
                    else:
                        break
                        
                current_chunk = overlap_chunk
                current_length = overlap_length

            current_chunk.append(word)
            current_length += word_length

        # The remaining final chunk
        if current_chunk:
            chunks.append(" ".join(current_chunk))

        return chunks

    def split_document(self, doc: RawDocument) -> List[DocumentChunk]:
        """
        Takes a RawDocument, splits its content, and returns a list of
        DocumentChunk objects ready to be stored in the database.
        """
        text_chunks = self.split_text(doc.content)
        document_chunks = []
        
        for i, text in enumerate(text_chunks):
            # Chunk ID generation
            chunk_id = str(uuid.uuid4())
            
            chunk = DocumentChunk(
                chunk_id=chunk_id,
                document_name=doc.document_name,
                content=text,
                # Metadata preservation and chunk-specific information
                metadata={
                    **doc.metadata,
                    "chunk_index": i,
                    "chunk_size": len(text)
                }
            )
            document_chunks.append(chunk)
            
        return document_chunks