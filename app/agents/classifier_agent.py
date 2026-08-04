from langchain_core.messages import HumanMessage, SystemMessage
from app.agents.llm import llm


def classifier_agent(state):

    prompt = """
Classify this support ticket.

Return ONLY JSON.

{
  "category":"",
  "priority":"",
  "sentiment":""
}
"""

    response = llm.invoke([
        SystemMessage(content=prompt),
        HumanMessage(content=state["messages"][-1].content)
    ])

    return response

