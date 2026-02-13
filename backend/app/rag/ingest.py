"""
Ingest RBI KYC Master Direction documents
- Chunk documents
- Generate embeddings
- Store in FAISS vector DB
"""
#from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from sentence_transformers import SentenceTransformer
import os
import pickle

EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"
VECTOR_DB_PATH = "app/rag/faiss_index"

def load_rbi_documents():
    docs = []
    docs_path = "app/rag/rbi_docs"

    for file in os.listdir(docs_path):
        if file.endswith(".pdf"):
            with open(os.path.join(docs_path, file), "r", encoding="utf-8") as f:
                docs.append(Document(page_content=f.read()))
    return docs

def ingest_documents():
    documents = load_rbi_documents()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(documents)

    embedding_model = SentenceTransformer(EMBEDDING_MODEL_NAME)

    vectorstore = FAISS.from_documents(
        chunks,
        embedding=lambda x: embedding_model.encode(x).tolist()
    )

    os.makedirs(VECTOR_DB_PATH, exist_ok=True)
    with open(f"{VECTOR_DB_PATH}/index.pkl", "wb") as f:
        pickle.dump(vectorstore, f)

    print("RBI KYC documents ingested and indexed successfully.")

if __name__ == "__main__":
    ingest_documents()
