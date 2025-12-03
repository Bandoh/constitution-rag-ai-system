# Ghana Constitution RAG System

A Retrieval-Augmented Generation (RAG) system for querying Ghana's Constitution using local LLMs and vector search.

## Overview

This project implements a conversational AI system that answers questions about Ghana's Constitution. It uses:
- **Qdrant** for vector storage and similarity search
- **LlamaIndex** for document processing and retrieval
- **Ollama** for local LLM inference
- **HuggingFace embeddings** for document vectorization

## Features

- 📚 Semantic search through Ghana's Constitution
- 🤖 Natural language responses powered by local LLMs
- 🔍 Context-aware retrieval with top-k similarity matching
- 💬 Conversational interface with legal expertise
- 🔒 Runs entirely locally - no external API calls

## Prerequisites

- Python 3.8+
- Docker (for Qdrant)
- Ollama installed locally
- Intel XPU support (or modify to use CPU/GPU)

## Installation

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd <repo-name>
```

### 2. Install Python dependencies
```bash
pip install -r requirements.txt
```

### 3. Install and Setup Ollama

**For Linux:**
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

**For macOS:**
```bash
brew install ollama
```

**For Windows:**
Download from [ollama.com/download](https://ollama.com/download)

### 4. Start Ollama Server
```bash
ollama serve
```

Keep this terminal running. Open a new terminal for the next steps.

### 5. Pull an Ollama Model

Choose one of these models (or any other from [ollama.com/library](https://ollama.com/library)):

**Recommended models:**
```bash
# Fast and efficient (3.8GB)
ollama pull llama3.2

# More capable (4.7GB)
ollama pull mistral

# Larger, more accurate (7.4GB)
ollama pull llama3.1:8b

# Powerful option (26GB)
ollama pull llama3.1:70b
```

For this example, we'll use `llama3.2`:
```bash
ollama pull llama3.2
```

### 6. Start Qdrant Vector Database
```bash
docker run -p 6333:6333 -p 6334:6334 \
    -v "$(pwd)/qdrant_storage:/qdrant/storage:z" \
    qdrant/qdrant
```

### 7. Configure Environment Variables

Create a `.env` file in the root directory:
```env
# Ollama model name (must match the model you pulled)
MODEL_NAME=llama3.2

# HuggingFace embedding model
EMBEDDING_MODEL=BAAI/bge-small-en-v1.5

# Qdrant collection name
COLLECTION_NAME=ghana_constitution

# Path to your Constitution documents
DOCUMENT_PATH=./documents
```

**Note:** Update `MODEL_NAME` to match whichever Ollama model you pulled (e.g., `mistral`, `llama3.1:8b`, etc.)

## Usage

### 1. Place Constitution Documents
Add your Ghana Constitution documents (PDF, TXT, DOCX) to the `./documents` directory

### 2. Run the System
```bash
python main.py
```

### 3. Query Examples
```python
run_rag("What does the constitution say about land ownership?")
```

## Ollama Commands Reference

```bash
# List installed models
ollama list

# Run a model interactively
ollama run llama3.2

# Remove a model
ollama rm llama3.2

# Check Ollama version
ollama --version

# Stop Ollama server
# Press Ctrl+C in the terminal running 'ollama serve'
```

## Project Structure

```
.
├── db_parsing.py          # Qdrant client and embedding setup
├── document_parsing.py    # Document loading and indexing
├── model_initialization.py # Ollama LLM integration
├── retrieval_db.py        # RAG retrieval pipeline
├── main.py                # Entry point
├── documents/             # Constitution documents
├── .env                   # Environment configuration
└── qdrant_storage/        # Vector database storage
```

## Configuration

### Embedding Model
The system uses HuggingFace embeddings running on Intel XPU. Adjust the `device` parameter in `db_parsing.py`:
- `"xpu"` for Intel XPU
- `"cpu"` for CPU
- `"cuda"` for NVIDIA GPU

### Chunking Strategy
- **Chunk size**: 1024 tokens
- **Chunk overlap**: 200 tokens
- Configurable in `document_parsing.py`

### Retrieval
- **Top-k results**: 4 similar chunks
- Adjustable in `retrieval_db.py`

## How It Works

1. **Document Processing**: Constitution documents are loaded and split into chunks with overlap
2. **Vectorization**: Chunks are embedded using HuggingFace models and stored in Qdrant
3. **Query Processing**: User questions are embedded and matched against stored vectors
4. **Context Retrieval**: Top-k most relevant chunks are retrieved
5. **Response Generation**: Ollama generates natural responses using retrieved context

## Example Queries

```python
run_rag("What are the fundamental human rights?")
run_rag("Explain the separation of powers")
run_rag("What does the constitution say about land laws?")
run_rag("Who can become president of Ghana?")
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.


## Acknowledgments

- Ghana's Constitution documents
- LlamaIndex framework
- Qdrant vector database
- Ollama local LLM runtime
- HuggingFace embedding models