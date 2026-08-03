from typing import Annotated
from typing_extensions import TypedDict

from langgraph.graph.message import add_messages


class SupportState(TypedDict):
    messages: Annotated[list, add_messages]

    ticket_id: str
    customer_id: str

    status: str

    route: str
    
    knowledge: str

'''
Why MessagesState?

Because it automatically stores:

Human messages
AI messages
Tool messages

This is the recommended LangGraph approach.






'''