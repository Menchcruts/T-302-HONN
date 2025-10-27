from dataclasses import dataclass


@dataclass
class Pricing:
    name: str
    price: float
    id: int = None
