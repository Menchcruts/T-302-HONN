from contextlib import AbstractContextManager
from typing import List, Callable

from injector import Module, provider, singleton, multiprovider
from sqlalchemy.orm import Session

from common.database.database import Database
from common.database.mapping import Mapping
from movie.movie_mapping import MovieMapping
from pricing.pricing_mapping import PricingMapping
from subscription.subscription_mapping import SubscriptionMapping
from user.user_mapping import UserMapping
from common.infrastructure.settings import Settings


class AppModule(Module):
    def __init__(self, settings: Settings):
        self.__settings = settings

    @provider
    @singleton
    def provide_settings(self) -> Settings:
        return self.__settings

    @multiprovider
    @singleton
    def provide_mappings(self) -> List[Mapping]:
        # noinspection PyTypeChecker
        return [
            MovieMapping(),
            PricingMapping(),
            SubscriptionMapping(),
            UserMapping()
        ]

    @provider
    @singleton
    def provide_session_factory(self, database: Database) -> Callable[..., AbstractContextManager[Session]]:
        return database.session