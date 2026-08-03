from typing import Literal

TECHNICAL_KEYWORDS = [
    "internet",
    "wifi",
    "router",
    "vpn",
    "network",
    "email",
    "password",
    "login",
    "server",
    "connection",
]


def routing_node(state) -> dict:

    message = state["messages"][-1].content.lower()

    for keyword in TECHNICAL_KEYWORDS:
        if keyword in message:
            return {
                "route": "technical"
            }

    return {
        "route": "general"
    }