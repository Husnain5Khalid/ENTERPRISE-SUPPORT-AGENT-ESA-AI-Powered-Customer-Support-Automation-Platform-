from langchain_core.tools import tool

@tool
def update_ticket(ticket_id:str, status:str):
    """Update the status of a support ticket."""

    