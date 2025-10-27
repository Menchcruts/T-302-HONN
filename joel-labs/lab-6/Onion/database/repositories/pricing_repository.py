from contextlib import AbstractContextManager
from typing import Callable

from injector import inject
from sqlalchemy.orm import Session
from core.entities.pricing import Pricing
from core.interfaces.IPricingRepo import IPricingRepository


class PricingRepository(IPricingRepository):
    @inject
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]):
        self.__session_factory = session_factory

    def get_all(self) -> list[Pricing]:
        with self.__session_factory() as session:
            return session.query(Pricing).all()

    def create_pricing(self, pricing: Pricing) -> None:
        with self.__session_factory() as session:
            session.add(pricing)
            session.commit()
            session.refresh(pricing)
