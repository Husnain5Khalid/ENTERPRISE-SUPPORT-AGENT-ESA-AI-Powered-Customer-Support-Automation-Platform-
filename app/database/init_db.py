## Initialized The DataBase

from app.database.base import Base
from app.database.database import engine

# Import models
from app.models.customer import Customer
from app.models.ticket import Ticket
from app.models.audit_log import AuditLog


def create_database():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    create_database()
    print("Database created successfully.")


