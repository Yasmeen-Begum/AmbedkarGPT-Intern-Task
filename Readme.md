# AmbedkarGPT – Intern Task (Kalpit Pvt Ltd UK)

A functional prototype Q&A system using **LangChain + ChromaDB + HuggingFace Embeddings + Ollama (Mistral 7B)**.

This project implements a simple RAG (Retrieval-Augmented Generation) pipeline that answers questions based only on Dr. B.R. Ambedkar's text from *Annihilation of Caste*.

---

## 🚀 Features
- Loads `speech.txt`
- Splits text into chunks
- Creates embeddings using `all-MiniLM-L6-v2`
- Stores embeddings locally in **ChromaDB**
- Retrieves relevant chunks via similarity search
- Generates answers using **Ollama + Mistral 7B**
- 100% local — no API keys

---

## 📦 Installation

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/AmbedkarGPT-Intern-Task
cd AmbedkarGPT-Intern-Task
```
### 2. Create a virtual environment
```
python3 -m venv venv
source venv/bin/activate     # Linux/Mac
venv\Scripts\activate        # Windows
```
### 3. Install dependencies
```
pip install -r requirements.txt
```
Setup Ollama + Mistral

Install Ollama:
```
curl -fsSL https://ollama.ai/install.sh | sh
```
Pull Mistral 7B:
```
ollama pull mistral

```
Ensure Ollama is running in the background:
```
ollama serve
```
Run the Project
```
python main.py
```

