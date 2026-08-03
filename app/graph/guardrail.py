from langchain_core.messages import AIMessage


def guardrail_node(state):
    last_message = state["messages"][-1]

    content = last_message.content

    # Handle Gemini/OpenAI list-based content
    if isinstance(content, list):
        text = ""

        for item in content:
            if isinstance(item, dict):
                text += item.get("text", "")
            else:
                text += str(item)

        content = text

    content = str(content).lower()

    blocked_words = [
        "hack",
        "illegal",
        "password",
    ]

    if any(word in content for word in blocked_words):
        state["messages"][-1] = AIMessage(
            content="I cannot assist with that request."
        )

    return state

'''
Why?

Even if the LLM makes a mistake, this node prevents unsafe responses from reaching the customer.

'''

