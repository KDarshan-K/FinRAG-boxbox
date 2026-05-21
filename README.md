# 📈 FinRAG

## AI-Powered Financial Report Analysis using RAG

FinRAG is a Finance-focused Retrieval-Augmented Generation (RAG) system that enables users to upload financial reports and interact with them using natural language queries.

The project combines:
- Semantic Search
- Vector Embeddings
- FAISS Vector Database
- Groq LLMs
- Financial Document Retrieval

to generate contextual and grounded financial insights from PDFs such as:
- Annual Reports
- Earnings Reports
- SEC Filings
- Financial Statements

---

# 🚀 Features

- Upload financial PDF reports
- Extract text from documents
- Intelligent text chunking
- Semantic embeddings generation
- FAISS vector database integration
- Retrieval-Augmented Generation (RAG)
- Groq-powered LLM responses
- Context-aware financial question answering
- Finance-oriented prompting and retrieval

---

# 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Language | Python |
| Frontend | Streamlit |
| RAG Framework | LangChain |
| Vector Database | FAISS |
| Embeddings | Sentence Transformers |
| LLM Provider | Groq |
| Model | Llama 3.1 |
| PDF Processing | PyMuPDF |

---

# 🏗️ Project Architecture

```text
Financial PDF
       ↓
Text Extraction
       ↓
Chunking
       ↓
Embeddings
       ↓
FAISS Vector Store
       ↓
Retriever
       ↓
Groq LLM
       ↓
Contextual Financial Answer
```

---

# 📂 Folder Structure

```text
FinRAG/
│
├── app.py
├── requirements.txt
├── .env
│
├── data/
│
├── rag/
│   ├── __init__.py
│   ├── loader.py
│   ├── chunker.py
│   ├── embeddings.py
│   ├── vectorstore.py
│   ├── retriever.py
│   └── qa_chain.py
│
└── README.md
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone <your-repository-url>
cd FinRAG
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Setup Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

Get API key from:
https://console.groq.com/keys

---

# ▶️ Running the Project

```bash
streamlit run app.py
```

---

# 🔍 How It Works

## Step 1 — PDF Upload

Users upload financial reports such as:
- Tesla Annual Reports
- Apple 10-K Filings
- NVIDIA Earnings Reports

---

## Step 2 — Text Extraction

The system extracts raw text from PDFs using:
- PyMuPDF

---

## Step 3 — Chunking

Large financial documents are split into smaller semantic chunks using:
- RecursiveCharacterTextSplitter

This improves retrieval quality.

---

## Step 4 — Embeddings

Chunks are converted into vector embeddings using:
- sentence-transformers/all-MiniLM-L6-v2

Embeddings capture semantic meaning of text.

---

## Step 5 — Vector Storage

Embeddings are stored in:
- FAISS Vector Database

This enables semantic similarity search.

---

## Step 6 — Retrieval

When the user asks a question:
- Query embeddings are generated
- Similar chunks are retrieved from FAISS

---

## Step 7 — Response Generation

Retrieved chunks are passed to:
- Groq LLM (Llama 3.1)

The LLM generates grounded financial answers based on retrieved context.

---

# 💡 Example Questions

```text
What are Tesla's major business risks?
```

```text
Explain NVIDIA revenue growth.
```

```text
What are Apple's supply chain challenges?
```

```text
Summarize the company's financial performance.
```

---

# 🔄 Example Workflow

```text
User Query
     ↓
Embedding Generation
     ↓
FAISS Similarity Search
     ↓
Relevant Financial Chunks
     ↓
Groq LLM
     ↓
Financial Analysis Response
```

---

# ✅ Current Capabilities

- Single PDF financial analysis
- Semantic retrieval
- Context-aware answers
- Financial question answering
- Retrieval-Augmented Generation

---


