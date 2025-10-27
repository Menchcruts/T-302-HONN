from contextlib import AbstractContextManager
from re import sub
from typing import Callable

from injector import inject
from sqlalchemy.orm import Session,  joinedload
from models.pricing import Pricing
from models.subscription import Subscription
from models.user import User


class SubscriptionRepository:
    @inject
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]):
        self.__session_factory = session_factory

    def get_all(self) -> list[Subscription]:
        with self.__session_factory() as session:
            return session.query(Subscription) \
                .options(joinedload(Subscription.pricing)) \
                .options(joinedload(Subscription.user)) \
                .all()

    def create_subscription(self, subscription: Subscription) -> None:
        with self.__session_factory() as session:
            subscription.user = session.query(User).get(subscription.user_id)
            subscription.pricing = session.query(
                Pricing).get(subscription.pricing_id)
            session.add(subscription)
            session.commit()
            session.refresh(subscription.user)
            session.refresh(subscription.pricing)
