from llama_index.core.retrievers import VectorIndexRetriever
from real.document_parsing import get_index
from real.model_initialization import query_ollama


retriever = VectorIndexRetriever(
    index=get_index(),
    similarity_top_k=4
)


def run_rag(prompt):
    query_ollama(prompt=prompt, retriever=retriever)
    pass
