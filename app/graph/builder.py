from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode

from app.graph.state import SupportState
from app.graph.router import should_continue
from app.graph.guardrail import guardrail_node
from app.agents.support_agent import support_agent
from app.tools.registry import TOOLS
from app.agents.classifier_agent import classifier_agent

# Create graph
graph = StateGraph(SupportState)


# -----------------------------
# Nodes
# -----------------------------
graph.add_node("agent", support_agent)
graph.add_node("tools", ToolNode(TOOLS))
graph.add_node("guardrail", guardrail_node)


# -----------------------------
# Flow
# -----------------------------
graph.add_node("classifier", classifier_agent)

graph.add_edge(START, "classifier")
graph.add_edge("classifier", "agent")


graph.add_conditional_edges(
    "agent",
    should_continue,
    {
        "tools": "tools",
        "__end__": "guardrail",
    },
)


graph.add_edge("tools", "agent")

graph.add_edge("guardrail", END)


# -----------------------------
# Compile Graph
# -----------------------------
support_graph = graph.compile()