from app.services.customer_service import CustomerService

customer_service = CustomerService()


def customer_node(state):

    customer = customer_service.get_customer(
        state["customer_id"]
    )

    print("=" * 60)
    print("Customer Retrieved")
    print(customer)
    print("=" * 60)

    return {
        "customer": customer
    }

