from fastapi import APIRouter
from pydantic import BaseModel

from rag.pipeline import retrieve_context
from services.llm_service import generate_response
from memory.chat_memory import (
    save_message,
    get_history
)

router = APIRouter()


class ChatRequest(BaseModel):
    session_id: str
    question: str


@router.post("/chat")
async def chat(request: ChatRequest):

    print("STEP 1")

    history_rows = get_history(request.session_id)

    history = "\n".join(
        [f"{role}: {message}" for role, message in history_rows]
    )

    print("STEP 2")

    context = retrieve_context(request.question)

    print("STEP 3")

    prompt = f"""
You are a helpful AI assistant.

Rules:
1. Use Conversation History to answer questions about previous chats.
2. Use Document Context to answer questions about uploaded files.
3. If the answer exists in either History or Context, use it.
4. If you do not know the answer, say so honestly.

Conversation History:
{history}

Document Context:
{context}

Question:
{request.question}

Answer:
"""

    print("\n===== HISTORY =====")
    print(history)

    print("\n===== CONTEXT =====")
    print(context)

    answer = generate_response(prompt)

    print("STEP 4")

    save_message(
        request.session_id,
        "user",
        request.question
    )

    save_message(
        request.session_id,
        "assistant",
        answer
    )

    return {
        "answer": answer,
        "context": context
    }