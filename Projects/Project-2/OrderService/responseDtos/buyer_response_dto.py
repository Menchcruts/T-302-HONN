from dataclasses import dataclass
from typing import Optional


@dataclass
class BuyerResponseDTO:
    name: str
    email: str
    phone_number: str
    address: str
