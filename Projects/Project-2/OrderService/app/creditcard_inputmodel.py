from dataclasses import dataclass

@dataclass
class CreditCardInputModel:
    card_number: str
    expiration_month: int
    expiration_year: int
    cvc: int
    