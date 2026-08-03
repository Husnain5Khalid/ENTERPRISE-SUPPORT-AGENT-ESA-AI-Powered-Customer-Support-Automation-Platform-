## Audit Log Model Created

from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.database.base import Base


class AuditLog(Base):

    __tablename__ = "audit_logs"

    log_id: Mapped[str] = mapped_column(
        String,
        primary_key=True,
    )

    ticket_id: Mapped[str]

    action: Mapped[str]

    timestamp: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )