from dataclasses import dataclass
from credit_card import CreditCard

@dataclass
class Order:
    productId: int
    merchantId: int
    buyerId: int
    creditCard: CreditCard
    discount: float
