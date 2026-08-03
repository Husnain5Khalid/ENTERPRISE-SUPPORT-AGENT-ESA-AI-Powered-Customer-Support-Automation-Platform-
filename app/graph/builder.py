from langgraph.graph import START, END, StateGraph
from langgraph.prebuilt import ToolNode

from app.graph.state import SupportState
from app.graph.router import should_continue
from app.graph.guardrail import guardrail_node
from app.agents.support_agent import support_agent
from app.tools.registry import TOOLS


graph = StateGraph(SupportState)

graph.add_node("agent", support_agent)
graph.add_node("tools", ToolNode(TOOLS))
graph.add_node("guardrail", guardrail_node)

graph.add_edge(START, "agent")

graph.add_conditional_edges(
    "agent",
    should_continue,
    {
        "tools":"tools",
        "__end__":"guardrail",
    },
)

graph.add_edge("tools","agent")
graph.add_edge("guardrail",END)

support_graph = graph.compile()

