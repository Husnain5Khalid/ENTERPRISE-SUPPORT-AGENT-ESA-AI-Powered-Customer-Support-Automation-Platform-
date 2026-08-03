## Ticket Model

from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.database.base import Base


class Ticket(Base):

    __tablename__ = "tickets"

    ticket_id: Mapped[str] = mapped_column(
        String,
        primary_key=True,
    )

    customer_id: Mapped[str] = mapped_column(
        ForeignKey("customers.customer_id")
    )

    subject: Mapped[str]

    description: Mapped[str]

    status: Mapped[str]

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )