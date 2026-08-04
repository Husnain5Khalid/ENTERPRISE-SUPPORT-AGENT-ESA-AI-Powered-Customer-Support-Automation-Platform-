## Responsibility: Retrieve customer information.
from langchain_core.tools import tool
from app.database.customer_database import CUSTOMERS


@tool
def get_customer(customer_id: str) -> str:
    """
    Retrieve customer information using the customer ID.
    """

    customer = CUSTOMERS.get(customer_id)

    if customer is None:
        return "Customer not found."

    return (
        f"Customer Name: {customer['name']}\n"
        f"Plan: {customer['plan']}\n"
        f"Status: {customer['status']}\n"
        f"Region: {customer['region']}"
    )
