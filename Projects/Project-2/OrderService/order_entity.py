from dataclasses import dataclass

@dataclass
class OrderEntity:
    product_id: int
    merchant_id: int
    buyer_id: int
    card_number: str
    discount: float

