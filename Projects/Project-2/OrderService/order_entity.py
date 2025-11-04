from dataclasses import dataclass

@dataclass
class OrderEntity:
    productId: int
    merchantId: int
    buyerId: int
    cardNumber: str
    discount: float

