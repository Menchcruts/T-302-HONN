from dependency_injector import containers, providers

from app.product_repo import ProductRepository


class Container(containers.DeclarativeContainer):
    product_repo_provider = providers.Singleton(
        ProductRepository
    )