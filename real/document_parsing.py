# docker run -p 6333:6333 -p 6334:6334 \
#     -v "$(pwd)/qdrant_storage:/qdrant/storage:z" \
#     qdrant/qdrant

import os
from dotenv import load_dotenv
from llama_index.core import SimpleDirectoryReader, Settings, VectorStoreIndex,StorageContext
from real.db_parsing import get_embedding_model,get_vector_store


load_dotenv()

docs = SimpleDirectoryReader(os.getenv("DOCUMENT_PATH")).load_data()
Settings.embed_model = get_embedding_model()
Settings.chunk_size= 1024
Settings.chunk_overlap=200

def get_index()->VectorStoreIndex:

    storage_context = StorageContext.from_defaults(vector_store=get_vector_store())

    index = VectorStoreIndex.from_documents(
        documents=docs,
        storage_context=storage_context
    )
    return index
