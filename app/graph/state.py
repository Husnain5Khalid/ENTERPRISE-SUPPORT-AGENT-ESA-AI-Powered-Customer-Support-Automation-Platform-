from typing import Annotated
from typing_extensions import TypedDict

from langgraph.graph.message import add_messages


class SupportState(TypedDict):
    # Conversation
    messages: Annotated[list, add_messages]

    # Ticket Information
    ticket_id: str
    customer_id: str
    status: str

    # Customer Information
    customer: dict

    # AI Classification
    category: str
    priority: str
    sentiment: str

    # Routing
    route: str
    escalation: bool
    escalation_reason: str

    # RAG
    knowledge: str

'''
Why MessagesState?

Because it automatically stores:

Human messages
AI messages
Tool messages

This is the recommended LangGraph approach.






'''