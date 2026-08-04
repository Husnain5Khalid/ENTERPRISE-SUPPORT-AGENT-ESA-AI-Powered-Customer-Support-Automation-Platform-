from fastapi import APIRouter
from fastapi import Depends

from app.schemas.ticket import TicketRequest
from app.schemas.response import TicketResponse

from app.api.dependencies import get_support_service
from app.services.support_service import SupportService

router = APIRouter()

@router.post("/chat", response_model=TicketResponse)
def chat(request: TicketRequest, service: SupportService = Depends(get_support_service)):

    result = service.process_ticket(
        ticket_id="TKT-001",
        customer_id=request.customer_id,
        message=request.description,
    )

    status = "Escalated" if result["escalation"] else "Resolved"

    return TicketResponse(
        ticket_id="TKT-001",
        status=status,
        message=result["messages"][-1].content,
        escalation=result["escalation"],
    )