from langchain_core.messages import SystemMessage

from app.agents.llm import llm_with_tools
from app.prompts.system_prompt import SYSTEM_PROMPT


def support_agent(state):

    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        *state["messages"],
    ]

    response = llm_with_tools.invoke(messages)

    print("\n" + "=" * 80)
    print("Response Object:")
    print(response)

    print("\nContent:")
    print(response.content)

    print("\nTool Calls:")
    print(response.tool_calls)

    print("\nAdditional kwargs:")
    print(response.additional_kwargs)

    print("=" * 80 + "\n")

    return {
        "messages": [response]
    }