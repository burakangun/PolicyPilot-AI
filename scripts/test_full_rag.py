import sys
import io
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

ROOT_DIR = Path(__file__).parent.parent
sys.path.append(str(ROOT_DIR / "backend"))

from app.rag.document_loader import load_documents
from app.rag.txt_splitter import TextSplitter
from app.rag.vector_store import VectorStore
from app.rag.generator import LLMGenerator

def main():
    print("Preparing Documents")
    raw_docs_dir = ROOT_DIR / "data" / "raw_docs"
    
    if not raw_docs_dir.exists():
        print(f"ERROR: {raw_docs_dir} directory not found!")
        return

    documents = load_documents(raw_docs_dir)
    print(f"{len(documents)} documents read.")

    splitter = TextSplitter(chunk_size=1000, chunk_overlap=200)
    all_chunks = []
    for doc in documents:
        chunks = splitter.split_document(doc)
        all_chunks.extend(chunks)
    print(f"{len(all_chunks)} chunks created.")

    print("Preparing Vector Database")
    db_path = ROOT_DIR / "backend" / "chroma_db"
    store = VectorStore(persist_directory=str(db_path), collection_name="policy_collection")
    store.add_chunks(all_chunks)
    print("Database updated.")

    print("RAG Query and Answer Generation")
    query = "Calisanlarin kisisel verileri nasil korunuyor?"
    print(f"Question: {query}")

    # Retrieval
    results = store.search(query=query, n_results=3)
    context_chunks = results['documents'][0]
    
    print(f"\n{len(context_chunks)} relevant chunks found. Generating answer...")

    # Generation
    generator = LLMGenerator()
    answer = generator.generate_answer(query, context_chunks)

    print("Answer :")
    print(answer)

if __name__ == "__main__":
    main()
