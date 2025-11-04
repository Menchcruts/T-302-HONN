from dependency_injector import containers, providers

from order_repository import OrderRepository
from order_service import OrderService
from order_event_publisher import OrderEventPublisher


class Container(containers.DeclarativeContainer):
    order_repository_provider = providers.Singleton(
        OrderRepository
    )

    order_service_provider = providers.Singleton(
        OrderService
    )

    order_event_publisher = providers.Singleton(
        OrderEventPublisher
    )
