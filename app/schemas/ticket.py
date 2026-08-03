from pydantic import BaseModel, Field

class TicketRequest(BaseModel):
    customer_id: str = Field(...)

    subject: str = Field(...)

    description:str = Field(...)

    