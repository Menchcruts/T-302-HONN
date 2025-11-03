from dataclasses import dataclass

@dataclass
class CreditCard:
    cardNumber: str
    expirationMonth: int
    expirationYear: int
    cvc: int
    