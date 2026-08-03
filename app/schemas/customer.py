from pydantic import BaseModel

class CustomerResponse(BaseModel):

    customer_id: str
    name: str
    email: str
    tier: str

    