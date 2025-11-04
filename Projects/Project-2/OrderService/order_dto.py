from dataclasses import dataclass

@dataclass
class OrderDTO:
    productId: int
    merchantId: int
    buyerId: int
    cardNumber: str
    totalPrice: float

