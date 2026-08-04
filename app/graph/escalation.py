from langchain_core.messages import AIMessage


def escalation_node(state):
    content = state["messages"][-1].content

    if isinstance(content, list):
        content = "".join(
            item["text"]
            for item in content
            if item.get("type") == "text"
        )

    message = content.lower()

    # rest of your logic

    reason = None

    if "refund" in message:
        reason = "Refund Request"

    elif "fraud" in message:
        reason = "Fraud"

    elif "legal" in message:
        reason = "Legal Complaint"

    elif state.get("priority") == "Critical":
        reason = "Critical Priority"

    if reason:
        return {
            **state,
            "escalation": True,
            "escalation_reason": reason,
            "messages": [
                AIMessage(
                    content=f"""
Your request has been escalated.

Reason: {reason}

A human support specialist will contact you shortly.
"""
                )
            ]
        }

    return {
        **state,
        "escalation": False,
        "escalation_reason": "",
    }

