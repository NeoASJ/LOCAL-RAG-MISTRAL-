RagNeoIQ Question Answer Bot
A Streamlit-based application for advanced Retrieval-Augmented Generation (RAG), document Q&A, and semantic search powered by Python, Ollama, ChromaDB, and LangChain.

🚀 Highlights
Upload PDFs: Add any PDF and automatically preprocess/split for semantic search.

Vector Search Engine: Uses ChromaDB with Ollama embeddings (“nomic-embed-text”) for fast, relevant retrieval.

Contextual Q&A: Combines context retrieval, re-ranking (MS MARCO Cross Encoder), and Mistral 7B-Instruct for robust answers.

Secure Environment: Easily exclude API keys and secrets via .gitignore for safe code sharing.

Intuitive UI: Streamlit interface supports easy doc uploads, queries, and exploration of search results.

📂 Project Structure
text
root/
├── app.py               # Main Streamlit application
├── new.py, TEX1.py      # Additional scripts
├── requirements.txt     # Dependencies
├── .env                 # Secrets & local config (excluded)
├── demo-rag-chroma/     # VectorDB index files
├── storage/             # Local storage
├── venv/                # Python virtual environment
└── data/                # Project data (optional)
🛠️ Installation & Usage
Prerequisites
Python 3.10+

Ollama (local server)

ChromaDB

Streamlit

Setup
Clone repository:

text
git clone <YOUR_REPO_URL>
cd lang
Create & activate virtual environment:

text
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
Install dependencies:

text
pip install -r requirements.txt
Add secret keys to .env:

Never share .env in version control. Add .env to .gitignore before pushing.

Start Ollama server:

text
ollama serve
Run Streamlit app:

text
streamlit run app.py
🎯 Key Features
PDF document ingest with intelligent text splitting and metadata management.

Query any document with semantic search and re-ranking pipelines.

View retrieved documents and top relevant passages.

Professional code structure with modular functions for future extensions.

🧩 Tech Stack
Technology	Purpose
Python	Core language
Streamlit	Web UI
Ollama	Embeddings & LLM orchestration
ChromaDB	Vector database for semantic search
LangChain	Document loaders, text splitting
MS MARCO CrossEncoder	Document re-ranking
