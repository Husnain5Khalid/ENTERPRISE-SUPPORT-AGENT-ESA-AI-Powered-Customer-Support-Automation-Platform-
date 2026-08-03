from langchain_core.tools import tool

@tool
def escalate_ticket(ticket_id:str, reason:str) -> str:
    """Escalate a support ticket to the appropriate support team."""
