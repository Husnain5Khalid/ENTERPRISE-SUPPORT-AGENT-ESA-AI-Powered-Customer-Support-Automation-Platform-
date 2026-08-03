from pydantic import BaseModel

class TicketResponse(BaseModel):
    ticket_id: str
    status: str
    message: str