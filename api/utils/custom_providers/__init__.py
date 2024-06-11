import random
import string

from faker.providers import DynamicProvider

medical_professions_provider = DynamicProvider(
    provider_name="medical_profession",
    elements=["dr.", "doctor", "nurse", "surgeon", "clerk"],
)

payment_method_provider = DynamicProvider(
    provider_name="payment_method",
    elements=["credit", "debit", "invoice"],
)

delivery_status_provider = DynamicProvider(
    provider_name="delivery_status",
    elements=["Delivered", "At Warehouse", "Shipped", "On Delivery Vehicle", "Cancelled"],
)


def get_record_locator(length=6):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))


record_locator_provider = DynamicProvider(
    provider_name="record_locator",
    elements=[get_record_locator() for _ in range(100)]
)

