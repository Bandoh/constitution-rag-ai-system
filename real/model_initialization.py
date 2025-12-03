from ollama import chat
from dotenv import load_dotenv
import os
from llama_index.core.retrievers import VectorIndexRetriever
load_dotenv()
from llama_index.llms.ollama import Ollama



def get_ollama_model()->Ollama:
    llm = Ollama(
    model=os.getenv("MODEL_NAME"),
    request_timeout=120.0,
    temperature=0.7,
    )
    return llm




def query_ollama(prompt: str, retriever:VectorIndexRetriever) -> str:

    retrieved_nodes = retriever.retrieve(prompt)
    cxt = "\n\n".join([node.text for node in retrieved_nodes])
    
    stream = chat(
        model=os.getenv("MODEL_NAME"),
        messages=[
            {
                'role': 'system', 
                'content': (
                    "You are a Ghanaian lawyer. "
                    "Do NOT use phrases like 'based on', 'according to', 'the text says', etc. "
                    "Answer naturally and directly."
                )
            },
            {
                'role': 'user',
                'content': f"Context:\n{cxt}"
            },
            {
                'role': 'user',
                'content': prompt
            }
        ],
        stream=True,
    )


    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)
    print("\n")


