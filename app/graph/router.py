from langgraph.prebuilt import tools_condition

def should_continue(state):
    return tools_condition(state)


'''
You don't need to write custom routing logic.

tools_condition() already checks whether the last AI message contains tool calls

'''

