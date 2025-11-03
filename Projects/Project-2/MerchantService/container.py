from dependency_injector import containers, providers

from repo.merchant_repository import MerchantRepository


class Container(containers.DeclarativeContainer):
    merchant_repository_provider = providers.Singleton(
        MerchantRepository
    )
