from langgraph.prebuilt import tools_condition

def should_continue(state):

    if state["route"] == "technical":
        return "knowledge"

    return "agent"


'''
You don't need to write custom routing logic.

tools_condition() already checks whether the last AI message contains tool calls

'''

