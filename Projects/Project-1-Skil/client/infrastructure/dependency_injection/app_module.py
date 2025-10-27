from injector import Module, provider, singleton

from client.infrastructure.settings.settings import Settings

from client.services.order_service import OrderService
from client.services.payment_service_stub import PaymentServiceStub
from client.repositories.order_repository import OrderRepository

from client.infrastructure.logging.client_logger_adapter import ClientLoggerAdapter
from client.infrastructure.logging.i_logger import ILogger

from client.infrastructure.logging.logger_config_factory import create_logger_config
from structured_logging.logger_creation.logger_config_builder import LoggerConfigBuilder


class AppModule(Module):
    def __init__(self, settings: Settings) -> None:
        self.__settings = settings

    @provider
    def provide_orderservice(self, repo: OrderRepository, payment: PaymentServiceStub, logger: ILogger) -> OrderService:
        return OrderService(payment, repo, logger)

    @provider
    def provide_repo(self) -> OrderRepository:
        return OrderRepository(self.__settings)

    @provider
    def provide_paymentstub(self, logger: ILogger) -> PaymentServiceStub:
        return PaymentServiceStub(self.__settings, logger)

    @provider
    @singleton
    def provide_client_logger(self) -> ILogger:
        config = create_logger_config(self.__settings, LoggerConfigBuilder())
        return ClientLoggerAdapter(config)