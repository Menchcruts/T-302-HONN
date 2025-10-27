from abc import ABC, abstractmethod
from core.entities.subscription import Subscription

class ISubscriptionRepository(ABC):
    @abstractmethod
    def get_all(self) -> list[Subscription]: ...

    @abstractmethod
    def create_subscription(self, subscription: Subscription) -> None: ...