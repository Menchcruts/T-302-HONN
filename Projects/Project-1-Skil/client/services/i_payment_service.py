from abc import ABC, abstractmethod
from client.models.payment import Payment


class IPaymentService(ABC):
    @abstractmethod
    def pay(self, payment: Payment):
        pass
