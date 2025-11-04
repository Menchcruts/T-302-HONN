from dataclasses import dataclass
from typing import Optional

from creditcard_inputmodel import CreditCardInputModel

@dataclass
class OrderInputModel:
    productId: int
    merchantId: int
    buyerId: int
    creditCard: CreditCardInputModel
    discount: Optional[float] = None
