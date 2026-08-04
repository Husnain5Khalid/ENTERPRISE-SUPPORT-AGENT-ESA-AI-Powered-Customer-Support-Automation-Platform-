from langchain_core.messages import HumanMessage, SystemMessage

from app.agents.llm import llm
from app.utils.parser import parse_json


def classifier_agent(state):

    prompt = """
You are a customer support ticket classifier.

Classify the ticket.

Return ONLY valid JSON.

{
  "category": "",
  "priority": "",
  "sentiment": "",
  "route": ""
}

Possible routes:
- technical
- billing
- refund
- general
"""

    response = llm.invoke([
        SystemMessage(content=prompt),
        HumanMessage(content=state["messages"][-1].content)
    ])

    content = response.content
    if isinstance(content, list):
        content = "".join(
            item["text"]
            for item in content
            if item.get("type") == "text"
        )
    result = parse_json(content)

    return {
    "category": result.get("category", "General Inquiry"),
    "priority": result.get("priority", "Medium"),
    "sentiment": result.get("sentiment", "Neutral"),
    "route": result.get("route", "general"),
    }
