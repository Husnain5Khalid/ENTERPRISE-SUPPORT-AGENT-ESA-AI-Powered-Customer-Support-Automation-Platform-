from langchain_core.messages import SystemMessage

from app.agents.llm import llm
from app.prompts.system_prompt import SYSTEM_PROMPT


def support_agent(state):
    """
    Generate the final response using the retrieved knowledge.
    """

    knowledge = state.get("knowledge", "")
    customer = state.get("customer", {})

    messages = [
        SystemMessage(
    content=f"""
{SYSTEM_PROMPT}

Customer Information

{customer}

Company Knowledge

{knowledge}

Use both customer information and company knowledge before answering.

Never invent information.
"""

        ),
        *state["messages"],
    ]

    response = llm.invoke(messages)

    return {
        "messages": [response]
    }
