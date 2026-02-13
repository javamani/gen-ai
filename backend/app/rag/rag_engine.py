"""
Retrieve relevant RBI KYC compliance rules using LangChain + FAISS
"""

import pickle
from sentence_transformers import SentenceTransformer

VECTOR_DB_PATH = "backend/app/faiss_index/index.pkl"
EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"

embedding_model = SentenceTransformer(EMBEDDING_MODEL_NAME)

def load_vectorstore():
    with open(VECTOR_DB_PATH, "rb") as f:
        return pickle.load(f)

def retrieve_compliance_rules(query: str, top_k: int = 3):
    vectorstore = load_vectorstore()
    query_embedding = embedding_model.encode(query).tolist()

    docs = vectorstore.similarity_search_by_vector(
        query_embedding,
        k=top_k
    )

    return [doc.page_content for doc in docs]
