## This is the only class that knows how to execute the graph.

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

        last_message = result["messages"][-1]
        content = last_message.content

        # Handle plain string
        if isinstance(content, str):
            return content

        # Handle Gemini content
        if isinstance(content, list):
            text = []

            for part in content:
                if isinstance(part, dict):
                    text.append(part.get("text", ""))
                else:
                    text.append(str(part))

            return "\n".join(text)

        return str(content)



'''
Why use a service?

Without it:

FastAPI

↓

Graph

Bad.

Instead:

FastAPI

↓

Support Service

↓

Graph









'''
                
                
                
        