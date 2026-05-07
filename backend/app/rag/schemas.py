from pydantic import BaseModel, Field


class RawDocument(BaseModel):
    document_name: str
    content: str
    metadata: dict = Field(default_factory=dict)

class DocumentChunk(BaseModel):
    chunk_id: str
    document_name: str
    section: str | None = None
    content: str
    metadata: dict = Field(default_factory=dict)

    