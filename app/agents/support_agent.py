from langchain_core.messages import SystemMessage, HumanMessage

from app.agents.llm import llm_with_tools
from app.prompts.system_prompt import SYSTEM_PROMPT


def support_agent(state):
    """
    Main AI agent responsible for handling customer support requests.
    """

    messages = [
        SystemMessage(content=SYSTEM_PROMPT),

        # Customer context supplied by backend
        HumanMessage(
            content=f"Customer ID: {state['customer_id']}"
        ),

        # User's support message
        *state["messages"],
    ]

    response = llm_with_tools.invoke(messages)

    # ---------- Debug ----------
    print("\n" + "=" * 70)
    print("SUPPORT AGENT")
    print("=" * 70)

    print("\nMessages Sent:")
    for message in messages:
        print(f"{message.type}: {message.content}")

    print("\nLLM Response:")
    print(response)

    print("\nTool Calls:")
    print(response.tool_calls)

    print("=" * 70 + "\n")
    # ---------------------------

    return {
        "messages": [response]
    }