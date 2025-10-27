from time import sleep

from injector import Injector
from client.infrastructure.dependency_injection.app_module import AppModule
from client.infrastructure.settings.settings import Settings
from client.models.order import Order
from client.models.payment import Payment
from client.services.order_service import OrderService


if __name__ == '__main__':
    settings = Settings()
    injector = Injector(AppModule(settings))
    order_service = injector.get(OrderService)

    order_service.place_order(Order(
        description="Test order",
        payment=Payment(
            amount=100,
            card_number="1234-1234-1234-1234",
            card_holder="John Doe",
            expiration_date="01/01/2021",
            security_code="123"
        )
    ))

    if settings.logging_is_async:
        sleep(settings.logging_async_delay + 2)
