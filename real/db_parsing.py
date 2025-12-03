


import os
from dotenv import load_dotenv
from qdrant_client import QdrantClient
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.vector_stores.qdrant import QdrantVectorStore

load_dotenv()

def get_qdrant_client()-> QdrantClient:
    client = QdrantClient(url="http://localhost:6333")
    return client

def get_embedding_model()->HuggingFaceEmbedding:
    embed_model = HuggingFaceEmbedding(
    model_name= os.getenv("EMBEDDING_MODEL"),
    device="xpu",
    embed_batch_size=8,
)
    return embed_model

def get_vector_store()->QdrantVectorStore:
    vec_store = QdrantVectorStore(
    client=get_qdrant_client(), collection_name=os.getenv("COLLECTION_NAME")
)
    return vec_store

