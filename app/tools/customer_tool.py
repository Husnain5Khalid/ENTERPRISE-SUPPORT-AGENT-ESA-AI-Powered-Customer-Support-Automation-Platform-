## Responsibility: Retrieve customer information.
from langchain_core.tools import tool
@tool
def get_customer(customer_id:str) -> dict:
    """Retrieve customer information by customer ID."""
    

    
