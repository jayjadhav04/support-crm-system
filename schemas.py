from pydantic import BaseModel


# Create Ticket Schema
class TicketCreate(BaseModel):

    customer_name: str

    customer_email: str

    subject: str

    description: str


# Update Ticket Schema
class TicketUpdate(BaseModel):

    status: str