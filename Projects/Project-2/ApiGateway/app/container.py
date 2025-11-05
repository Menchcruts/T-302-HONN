from dependency_injector import containers, providers

from app.gateway_service import GatewayService



class Container(containers.DeclarativeContainer):
    gateway_service_provider = providers.Singleton(
        GatewayService
    )
