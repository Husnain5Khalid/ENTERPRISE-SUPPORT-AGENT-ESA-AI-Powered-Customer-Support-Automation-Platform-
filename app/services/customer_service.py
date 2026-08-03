from app.database.customer_database import CUSTOMERS


class CustomerService:

    def get_customer(self, customer_id: str):

        return CUSTOMERS.get(
            customer_id,
            {
                "name": "Unknown",
                "status": "Unknown"
            }
        )

    