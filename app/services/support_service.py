from langchain_core.messages import HumanMessage

from app.graph.builder import support_graph


class SupportService:

    def process_ticket(
        self,
        ticket_id: str,
        customer_id: str,
        message: str,
    ):

        state = {
            "messages": [
                HumanMessage(content=message)
            ],
            "ticket_id": ticket_id,
            "customer_id": customer_id,
        }

        result = support_graph.invoke(state)

        return result