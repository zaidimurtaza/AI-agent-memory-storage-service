from fastapi import APIRouter, HTTPException

from app.memory_manager import add_message, get_messages, list_conversations
from app.schema import Message

router = APIRouter(prefix="/chat", tags=["memory"])


@router.get("/")
def get_conversations():
    """List all conversation IDs."""
    return {"conversations": list_conversations()}


@router.post("/{conversation_id}/messages")
def post_message(conversation_id: str, message: Message):
    """Add a message. Creates conversation on first message."""
    msg = add_message(conversation_id, message.role, message.content)
    return {"message": msg}


@router.get("/{conversation_id}")
def get_history(conversation_id: str, limit: int | None = None):
    """Get conversation history. ?limit=N for last N messages (context window)."""
    messages = get_messages(conversation_id, limit)
    if not messages and conversation_id not in list_conversations():
        raise HTTPException(404, "Conversation not found")
    return {"conversation_id": conversation_id, "messages": messages}
