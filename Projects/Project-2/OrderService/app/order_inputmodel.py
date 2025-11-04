from dataclasses import dataclass
from typing import Optional

from .creditcard_inputmodel import CreditCardInputModel

@dataclass
class OrderInputModel:
    product_id: int
    merchant_id: int
    buyer_id: int
    credit_card: CreditCardInputModel
    discount: Optional[float] = None
