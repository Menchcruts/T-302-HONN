from dataclasses import dataclass
from client.models.payment import Payment


@dataclass
class Order:
    description: str
    payment: Payment
