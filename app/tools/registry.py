from app.tools.knowledge_tool import search_knowledge
from app.tools.customer_tool import get_customer
from app.tools.ticket_tool import update_ticket
from app.tools.escalation_tool import escalate_ticket
from app.tools.audit_tool import log_action

TOOLS = [
    search_knowledge,

    get_customer,

    update_ticket,

    escalate_ticket,

    log_action


]