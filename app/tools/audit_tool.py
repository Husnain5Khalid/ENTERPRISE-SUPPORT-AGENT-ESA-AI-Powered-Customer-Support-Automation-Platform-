from langchain_core.tools import tool

@tool

def log_action(ticket_id:str, action:str) -> str:
    """Write an audit log entry for a support ticket."""

