from langgraph.graph import MessagesState


class SupportState(MessagesState):
    customer_id: str | None = None
    ticket_id: str | None = None
    intent: str | None = None
    customer: dict | None = None
    knowledge: list | None = None
    decision: str | None = None

'''
Why MessagesState?

Because it automatically stores:

Human messages
AI messages
Tool messages

This is the recommended LangGraph approach.






'''