from langchain_core.messages import SystemMessage

from app.agents.llm import llm
from app.prompts.system_prompt import SYSTEM_PROMPT


def support_agent(state):
    """
    Generate the final response using the retrieved knowledge.
    """

    knowledge = state.get("knowledge", "")

    messages = [
        SystemMessage(
            content=f"""
{SYSTEM_PROMPT}

You have access to the following knowledge retrieved from the company's internal documentation.

-------------------------
{knowledge}
-------------------------

Instructions:
- Use the retrieved knowledge to answer the customer's question.
- If the knowledge does not contain the answer, politely inform the customer that the issue will be escalated to the support team.
- Do not make up policies or troubleshooting steps.
- Keep the response concise and professional.
"""
        ),
        *state["messages"],
    ]

    response = llm.invoke(messages)

    return {
        "messages": [response]
    }
