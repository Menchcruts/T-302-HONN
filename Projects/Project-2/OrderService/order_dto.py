from dataclasses import dataclass

@dataclass
class OrderDTO:
    product_id: int
    merchant_id: int
    buyer_id: int
    card_number: str
    total_price: float

