# 🤖 Intelligent RAG Chatbot with Memory & Live Data Retrieval

A production-oriented **AI chatbot** built using **Retrieval-Augmented Generation (RAG)**, conversational memory, vector databases, user-uploaded documents, and real-time web retrieval.

The system is designed to answer questions using multiple sources:

* 🧠 Conversational memory
* 📄 User-uploaded documents
* 🔎 Vector database retrieval
* 🌐 Real-time web information
* 🤖 Large Language Models (LLMs)

---

## 🚀 Project Overview

Traditional chatbots depend only on the knowledge available inside the LLM.

This project combines an LLM with external knowledge sources using **Retrieval-Augmented Generation (RAG)**.

```text
                         ┌──────────────────┐
                         │      USER        │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │   Chat Interface │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │   Query Router   │
                         └──────┬─────┬─────┘
                                │     │
                  ┌─────────────┘     └──────────────┐
                  ▼                                  ▼
          ┌─────────────────┐                ┌─────────────────┐
          │ Conversation    │                │   Web Search    │
          │ Memory          │                │   / Live Data   │
          └────────┬────────┘                └────────┬────────┘
                   │                                  │
                   └──────────────┬───────────────────┘
                                  ▼
                         ┌──────────────────┐
                         │ RAG Retriever    │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │ Vector Database  │
                         │    ChromaDB      │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │ Context Builder  │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │      LLM         │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │ Final Response   │
                         └──────────────────┘
```

---

# ✨ Features

## 🧠 Conversational Memory

The chatbot maintains conversation context across multiple messages.

Example:

```text
User:
My name is Alex.

Bot:
Nice to meet you, Alex!

User:
What is my name?

Bot:
Your name is Alex.
```

Memory can be maintained using:

* Session memory
* Conversation history
* Persistent memory
* Vector-based memory

---

## 📚 RAG Document Retrieval

Users can upload documents and ask questions about them.

Supported formats:

* PDF
* TXT
* DOCX
* CSV
* XLSX

Example:

```text
User uploads:
company_policy.pdf

User:
What is the annual leave policy?

Bot:
According to the uploaded company policy...
```

The chatbot retrieves relevant sections instead of sending the entire document to the LLM.

---

# 🌐 Live Information Retrieval

The chatbot can retrieve current information from external sources when required.

Examples:

```text
What is the current weather?

What are today's major news headlines?

What is the latest Python version?

What happened in the stock market today?
```

This prevents the chatbot from relying only on outdated LLM knowledge.

---

# ⏰ Current Time

The system can answer current-time questions using the appropriate timezone.

Example:

```text
User:
What time is it in India?

Bot:
The current time in India is...
```

---

# 📂 Dynamic File Upload

Users can upload new documents at runtime.

The system automatically:

```text
Upload File
     ↓
Detect File Type
     ↓
Extract Text
     ↓
Clean Data
     ↓
Chunk Documents
     ↓
Generate Embeddings
     ↓
Store in Vector Database
     ↓
Ready for Retrieval
```

Newly uploaded information becomes available to the chatbot without rebuilding the entire application.

---

# 🧩 RAG Architecture

The RAG pipeline consists of:

### 1. Document Loading

Documents are loaded from:

```text
PDF
TXT
DOCX
CSV
XLSX
```

### 2. Text Extraction

Content is extracted from uploaded files.

### 3. Text Chunking

Large documents are divided into smaller chunks.

Example:

```text
Original Document
       ↓
Large Text
       ↓
Chunk 1
Chunk 2
Chunk 3
Chunk 4
...
```

### 4. Embeddings

Each chunk is converted into a numerical vector representation.

```text
Text
 ↓
Embedding Model
 ↓
Vector
```

### 5. Vector Database

Embeddings are stored inside a vector database.

This project uses:

```text
ChromaDB
```

### 6. Semantic Retrieval

When the user asks a question:

```text
Question
   ↓
Question Embedding
   ↓
Similarity Search
   ↓
Relevant Chunks
```

### 7. Context Augmentation

The retrieved information is added to the LLM prompt.

### 8. Response Generation

The LLM generates the final answer using the retrieved context.

---

# 🧠 Memory Architecture

The chatbot uses memory separately from document retrieval.

```text
                  USER MESSAGE
                       │
                       ▼
              ┌─────────────────┐
              │ Memory Manager  │
              └────────┬────────┘
                       │
            ┌──────────┴──────────┐
            ▼                     ▼
    Short-Term Memory      Long-Term Memory
            │                     │
            ▼                     ▼
      Conversation          Persistent Store
       Context
```

This allows the chatbot to understand both:

```text
"What did I just say?"
```

and

```text
"What information do you remember about me?"
```

---

# 🛠️ Technology Stack

| Component            | Technology                                         |
| -------------------- | -------------------------------------------------- |
| Programming Language | Python                                             |
| Backend              | FastAPI                                            |
| Frontend             | Streamlit                                          |
| RAG Framework        | LangChain                                          |
| Vector Database      | ChromaDB                                           |
| LLM                  | Ollama / Gemini / OpenAI                           |
| Embeddings           | Sentence Transformers / compatible embedding model |
| Document Processing  | PyPDF, python-docx, pandas, openpyxl               |
| API Testing          | Swagger / Postman                                  |
| Containerization     | Docker                                             |
| Database             | PostgreSQL                                         |
| Version Control      | Git + GitHub                                       |

---

# 📁 Project Structure

```text
rag-chatbot/
│
├── app/
│   ├── main.py
│   ├── config.py
│   └── dependencies.py
│
├── routes/
│   ├── chat_routes.py
│   └── upload_routes.py
│
├── rag/
│   ├── pipeline.py
│   ├── retriever.py
│   ├── chunking.py
│   └── embeddings.py
│
├── memory/
│   ├── chat_memory.py
│   └── session_manager.py
│
├── vectorstore/
│   └── chroma_store.py
│
├── services/
│   ├── llm_service.py
│   ├── web_search.py
│   └── file_service.py
│
├── frontend/
│   └── app.py
│
├── uploads/
│
├── data/
│   └── chroma_db/
│
├── logs/
│
├── tests/
│
├── .env
├── .gitignore
├── requirements.txt
├── docker-compose.yml
└── README.md
```

---

# 🔄 Complete Data Flow

```text
                    USER
                     │
                     ▼
              Chat Interface
                     │
                     ▼
              FastAPI Backend
                     │
                     ▼
               Query Router
                     │
        ┌────────────┼────────────┐
        │            │            │
        ▼            ▼            ▼
     Memory        RAG         Web Search
        │            │            │
        │            ▼            │
        │       ChromaDB          │
        │            │            │
        └────────────┼────────────┘
                     ▼
               Context Builder
                     │
                     ▼
                    LLM
                     │
                     ▼
             Final Answer
                     │
                     ▼
                   USER
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/rag-chatbot.git
```

Move into the project:

```bash
cd rag-chatbot
```

---

# 🐍 2. Create Virtual Environment

Create the environment:

```bash
python3 -m venv venv
```

Activate it on macOS/Linux:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

---

# 📦 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔐 4. Environment Variables

Create a `.env` file:

```env
APP_NAME=RAG Chatbot
DEBUG=True

LLM_PROVIDER=ollama

OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3

GOOGLE_API_KEY=your_google_api_key

OPENAI_API_KEY=your_openai_api_key

CHROMA_DB_PATH=./data/chroma_db

DATABASE_URL=postgresql://username:password@localhost:5432/ragdb
```

Never commit `.env` to GitHub.

Add it to `.gitignore`:

```text
.env
venv/
__pycache__/
data/chroma_db/
uploads/
logs/
*.pyc
```

---

# 🦙 5. Running Ollama

If using Ollama:

```bash
ollama serve
```

Then pull the model:

```bash
ollama pull llama3
```

Verify:

```bash
ollama list
```

---

# 🚀 6. Start FastAPI

Run:

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

---

# 💬 7. Start Streamlit

Open another terminal:

```bash
streamlit run frontend/app.py
```

The chatbot UI will then be available through the Streamlit address shown in the terminal.

---

# 📤 File Upload Workflow

Example:

```text
User
 │
 ▼
Upload PDF
 │
 ▼
FastAPI
 │
 ▼
File Service
 │
 ▼
Text Extraction
 │
 ▼
Chunking
 │
 ▼
Embeddings
 │
 ▼
ChromaDB
 │
 ▼
Document Available
```

Then:

```text
User:
What does the document say about employee benefits?

       ↓

Retriever

       ↓

Relevant document chunks

       ↓

LLM

       ↓

Answer
```

---

# 🔎 Example API

## Chat Request

```http
POST /chat
```

Example request:

```json
{
    "session_id": "user_001",
    "question": "What is RAG?"
}
```

Example response:

```json
{
    "answer": "RAG stands for Retrieval-Augmented Generation...",
    "context": "...",
    "sources": []
}
```

---

# 📄 Upload Request

```http
POST /upload
```

Upload:

```text
company_policy.pdf
```

The application processes the document and adds it to the vector database.

---

# 🧪 Testing

Test the backend using:

```text
Swagger
Postman
pytest
```

Run tests:

```bash
pytest
```

Example test cases:

```text
✓ Basic chatbot question
✓ Memory retention
✓ Document retrieval
✓ PDF upload
✓ CSV retrieval
✓ Excel retrieval
✓ Web search
✓ Current-time question
✓ Invalid file handling
✓ Empty question handling
```

---

# 🧠 Example Conversations

### Conversation Memory

```text
User:
My name is Alex.

Bot:
Nice to meet you, Alex.

User:
What is my name?

Bot:
Your name is Alex.
```

---

### Document RAG

```text
User:
Upload employee_policy.pdf

Bot:
Document successfully processed.

User:
How many annual leave days are available?

Bot:
According to the uploaded document...
```

---

### Live Information

```text
User:
What are the latest developments in AI?

Bot:
I'll retrieve current information...
```

---

### Mixed Retrieval

The system can combine multiple sources:

```text
User Question
      │
      ├── Conversation Memory
      │
      ├── Uploaded Documents
      │
      ├── Vector Database
      │
      └── Live Web Data
              │
              ▼
        Context Fusion
              │
              ▼
             LLM
              │
              ▼
        Final Answer
```

---

# 🔐 Security Considerations

Production deployment should include:

* API authentication
* API authorization
* Input validation
* File validation
* File-size restrictions
* Rate limiting
* Secret management
* HTTPS
* Logging
* Error handling
* Prompt injection protection
* Data isolation between users
* Secure database credentials

---

# ⚡ Performance Optimization

Possible improvements:

* Async FastAPI endpoints
* Embedding caching
* Vector-search optimization
* Query rewriting
* Retrieval filtering
* Reranking
* Response streaming
* Redis caching
* Background document processing
* Batch embedding generation

---

# 🐳 Docker

Build the application:

```bash
docker compose build
```

Start services:

```bash
docker compose up
```

Run in background:

```bash
docker compose up -d
```

Stop services:

```bash
docker compose down
```

View logs:

```bash
docker compose logs -f
```

---

# 📊 Production Architecture

```text
                         ┌───────────────┐
                         │    Client     │
                         └───────┬───────┘
                                 │
                                 ▼
                         ┌───────────────┐
                         │   Frontend    │
                         └───────┬───────┘
                                 │
                                 ▼
                         ┌───────────────┐
                         │    FastAPI    │
                         │    Backend    │
                         └───────┬───────┘
                                 │
              ┌──────────────────┼──────────────────┐
              │                  │                  │
              ▼                  ▼                  ▼
        ┌───────────┐      ┌───────────┐      ┌───────────┐
        │  Memory   │      │    RAG    │      │ Web Search│
        └─────┬─────┘      └─────┬─────┘      └─────┬─────┘
              │                  │                  │
              ▼                  ▼                  │
        ┌───────────┐      ┌───────────┐            │
        │ PostgreSQL│      │ ChromaDB  │            │
        └───────────┘      └─────┬─────┘            │
                                 │                  │
                                 └────────┬─────────┘
                                          ▼
                                   ┌─────────────┐
                                   │     LLM     │
                                   └─────────────┘
```

---

# 🎯 Future Improvements

Planned enhancements:

* [ ] Multi-user authentication
* [ ] Long-term semantic memory
* [ ] Advanced query routing
* [ ] Hybrid search
* [ ] Reranking
* [ ] Agentic RAG
* [ ] Multimodal RAG
* [ ] Image/PDF vision support
* [ ] Voice input
* [ ] Voice output
* [ ] Streaming responses
* [ ] Redis caching
* [ ] PostgreSQL memory
* [ ] Observability
* [ ] LangSmith tracing
* [ ] Kubernetes deployment
* [ ] Cloud deployment
* [ ] CI/CD pipeline

---

# 📈 Learning Objectives

This project demonstrates practical knowledge of:

* Python
* FastAPI
* REST APIs
* RAG
* LLMs
* LangChain
* Vector databases
* Embeddings
* Semantic search
* Prompt engineering
* Conversational memory
* Document processing
* Web retrieval
* Docker
* PostgreSQL
* Git/GitHub
* AI application architecture

---

# 👨‍💻 Author

**Shifana**

Data Science & AI Enthusiast

Interested in:

* Artificial Intelligence
* Machine Learning
* Generative AI
* LLMs
* RAG
* Data Science
* Analytics

---

# ⭐ Project Goal

The goal of this project is to build a **professional, production-oriented AI chatbot** capable of combining:

```text
            ┌────────────────────┐
            │  User Conversation │
            └─────────┬──────────┘
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
       Memory       RAG       Live Data
          │           │           │
          └───────────┼───────────┘
                      ▼
                     LLM
                      │
                      ▼
              Intelligent Answer
```

This project serves as a practical implementation of **Retrieval-Augmented Generation + Conversational Memory + Real-Time Data Retrieval** using modern AI engineering practices.
