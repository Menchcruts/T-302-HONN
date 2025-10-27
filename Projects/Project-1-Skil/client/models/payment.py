from dataclasses import dataclass


@dataclass
class Payment:
    card_number: str
    expiration_date: str
    security_code: str
    card_holder: str
    amount: float
