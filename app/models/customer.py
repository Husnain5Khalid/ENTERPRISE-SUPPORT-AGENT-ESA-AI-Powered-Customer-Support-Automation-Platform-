# Customer Model

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class Customer(Base):
    __tablename__ = "customers"

    customer_id: Mapped[str] = mapped_column(
        String,
        primary_key=True,
    )

    name: Mapped[str]

    email: Mapped[str]

    tier: Mapped[str]