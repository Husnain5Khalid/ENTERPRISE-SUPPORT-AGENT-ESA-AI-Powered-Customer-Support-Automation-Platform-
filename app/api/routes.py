from fastapi import APIRouter, Depends

from app.api.dependencies import get_support_service
from app.schemas.ticket import TicketRequest
from app.schemas.response import TicketResponse
from app.services.support_service import SupportService
from app.utils.message import get_message_text

router = APIRouter()


@router.post("/chat", response_model=TicketResponse)
def chat(
    request: TicketRequest,
    service: SupportService = Depends(get_support_service),
):

    message = f"""
Subject: {request.subject}

Description:
{request.description}
"""

    result = service.process_ticket(
        ticket_id="TKT-001",      # Temporary until you add ticket generation
        customer_id=request.customer_id,
        message=message,
    )

    response_text = get_message_text(result["messages"][-1])

    status = "Escalated" if result.get("escalation", False) else "Resolved"

    return TicketResponse(
        ticket_id=result["ticket_id"],
        status=status,
        message=response_text,
    )