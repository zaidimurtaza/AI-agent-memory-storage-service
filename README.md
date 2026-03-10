# AI Memory Service

A FastAPI-based memory store for AI agent conversation history. Built to handle multi-turn conversations with support for context windows and conversation management.

## Features

- **Conversation Management** - Store and retrieve multi-turn conversations
- **Context Windows** - Limit message retrieval to last N messages
- **RESTful API** - Clean endpoints with auto-generated docs
- **Type Safety** - Full Pydantic validation
- **Fast & Async** - Built on FastAPI

## Quick Start

```bash
# Install dependencies
pip install fastapi uvicorn pydantic

# Run the service
uvicorn main:app --reload

# Visit http://localhost:8000/docs for interactive API docs
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Health check |
| `GET` | `/chat/` | List all conversations |
| `GET` | `/chat/{id}` | Get conversation history |
| `POST` | `/chat/{id}/messages` | Add a message |

## Usage Example

```bash
# Create a message
curl -X POST "http://localhost:8000/chat/conv-123/messages" \
  -H "Content-Type: application/json" \
  -d '{"role": "user", "content": "Hello!"}'

# Get conversation (with context window)
curl "http://localhost:8000/chat/conv-123?limit=10"
```

## Architecture

```
AI-Memory-Service/
├── main.py                # FastAPI app entry point
└── app/
    ├── routes.py          # API endpoints
    ├── memory_manager.py  # Storage logic
    └── schema.py          # Pydantic models
```

**Note**: Uses in-memory storage. For production, integrate a database (PostgreSQL, Redis, MongoDB).

## Built With

- FastAPI - Web framework
- Pydantic - Data validation
- Python 3.10+ - Type hints support
