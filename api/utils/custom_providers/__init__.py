from faker.providers import DynamicProvider

payment_method_provider = DynamicProvider(
    provider_name="payment_method",
    elements=["credit", "debit", "invoice"],
)

delivery_status_provider = DynamicProvider(
    provider_name="delivery_status",
    elements=["Delivered", "At Warehouse", "Shipped", "On Delivery Vehicle", "Cancelled"],
)
