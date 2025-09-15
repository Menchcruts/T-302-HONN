from dataclasses import dataclass
from enum import Enum

from models.Buyer import Buyer
from models.Merchant import Merchant


class OrderStatus(Enum):
    Cancelled = 0,
    Paid = 1,
    Unpaid = 2


@dataclass
class Order:
    merchant: Merchant
    buyer: Buyer
    status: OrderStatus
