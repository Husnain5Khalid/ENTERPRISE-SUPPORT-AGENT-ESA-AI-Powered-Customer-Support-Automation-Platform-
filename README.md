# Enterprise Support Agent (ESA)
### AI-Powered Customer Support Automation Platform

An enterprise-grade AI customer support system built with **FastAPI**, **LangGraph**, **LangChain**, **Google Gemini**, and **RAG (Retrieval-Augmented Generation)**.

The platform automates customer support by classifying tickets, retrieving relevant knowledge from company documentation, generating accurate responses, and deciding whether tickets should be resolved automatically or escalated.

---

# Features

- AI-powered customer support assistant
- LangGraph multi-agent workflow
- Google Gemini LLM integration
- Retrieval-Augmented Generation (RAG)
- Internal knowledge base search
- Automatic ticket classification
- Priority detection
- Sentiment analysis
- Automatic ticket resolution
- Human escalation workflow
- Guardrails for safe AI responses
- REST API using FastAPI
- Interactive Swagger documentation
- Docker support

---

# Project Architecture

```
Customer
    │
    ▼
 FastAPI API
    │
    ▼
 LangGraph Workflow
    │
    ├──────────────┐
    ▼              │
Classification     │
    │              │
    ▼              │
Resolution         │
    │              │
    ▼              │
Support Agent
    │
    ▼
Knowledge Search (RAG)
    │
    ▼
Gemini LLM
    │
    ▼
Guardrail
    │
    ▼
Final Response
```

---

# Tech Stack

- Python 3.12
- FastAPI
- LangGraph
- LangChain
- Google Gemini
- FAISS
- Sentence Transformers
- Pydantic
- Uvicorn
- Docker

---

# Project Structure

```
app/
│
├── agents/
├── api/
├── config/
├── graph/
├── prompts/
├── rag/
├── schemas/
├── services/
├── tools/
├── utils/
├── main.py
│
data/
│
├── documents/
├── vector_store/
│
Dockerfile
docker-compose.yml
requirements.txt
README.md
```

---

# Workflow

1. Customer submits a support ticket.
2. AI classifies the ticket.
3. Priority is detected.
4. Sentiment is analyzed.
5. Confidence score is calculated.
6. Resolution engine decides:
   - Resolve automatically
   - Escalate to human
7. Knowledge base is searched.
8. Gemini generates a response.
9. Guardrails verify the output.
10. API returns the final response.

---

# API Endpoint

```
POST /chat
```

Example Request

```json
{
  "customer_id": "CUS001",
  "subject": "Internet Issue",
  "description": "My internet is not working."
}
```

Example Response

```json
{
  "ticket_id": "TKT-001",
  "category": "Internet Issue",
  "priority": "High",
  "sentiment": "Negative",
  "confidence": 0.94,
  "status": "Resolved",
  "message": "Please restart your router and check whether the modem lights are stable."
}
```

---

# Running Locally

## Clone Repository

```bash
git clone <repository-url>
cd ENTERPRISE-SUPPORT-AGENT
```

## Create Virtual Environment

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Configure Environment

Create a `.env` file.

Example:

```text
GOOGLE_API_KEY=your_api_key
MODEL_NAME=gemini-3.5-flash-lite
```

## Start Server

```bash
uvicorn app.main:app --reload
```

Open:

```
http://localhost:8000/docs
```

---

# Docker

Build Image

```bash
docker build -t enterprise-support-agent .
```

Run Container

```bash
docker run -p 8000:8000 --env-file .env enterprise-support-agent
```

Or use Docker Compose

```bash
docker compose up --build
```

---

# Knowledge Base

The system uses Retrieval-Augmented Generation (RAG).

Pipeline:

```
Documents
     │
     ▼
Text Splitter
     │
     ▼
Embeddings
     │
     ▼
FAISS Vector Store
     │
     ▼
Retriever
     │
     ▼
Gemini
```

---

# AI Workflow

```
START
   │
   ▼
Classifier
   │
   ▼
Resolution
   │
   ▼
Support Agent
   │
   ▼
Knowledge Tool
   │
   ▼
Guardrail
   │
   ▼
END
```

---

# Future Improvements

- Authentication
- Conversation memory
- Ticket history
- Human approval workflow
- Monitoring and observability
- Admin dashboard
- PostgreSQL integration
- Redis caching
- Kubernetes deployment

---

# License

This project is provided for educational and portfolio purposes.

---

# Author
Husnain Khalid

Developed as an enterprise AI customer support platform using modern LLM engineering practices, LangGraph workflows, Retrieval-Augmented Generation (RAG), and FastAPI.
