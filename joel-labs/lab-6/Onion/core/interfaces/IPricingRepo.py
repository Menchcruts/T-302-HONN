from abc import ABC, abstractmethod
from core.entities.pricing import Pricing

class IPricingRepository(ABC):
    @abstractmethod
    def get_all(self) -> list[Pricing]: ...

    @abstractmethod
    def create_pricing(self, pricing: Pricing) -> None: ...