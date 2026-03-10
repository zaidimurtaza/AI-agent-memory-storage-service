from typing import Optional

from app.schema import Message

# Single shared store - one dict for all conversations
store: dict[str, list[Message]] = {}


def add_message(conversation_id: str, role: str, content: str) -> Message:
    """Add a message. Creates conversation if it doesn't exist."""
    if conversation_id not in store:
        store[conversation_id] = []
    msg = Message(role=role, content=content)
    store[conversation_id].append(msg)
    return msg


def get_messages(conversation_id: str, limit: Optional[int] = None) -> list[Message]:
    """Get messages. Use limit for last N (context window)."""
    messages = store.get(conversation_id, [])
    return messages[-limit:] if limit else messages


def list_conversations() -> list[str]:
    """List all conversation IDs."""
    return list(store.keys())
