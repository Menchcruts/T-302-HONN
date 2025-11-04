from dataclasses import dataclass

@dataclass
class CreditCardInputModel:
    cardNumber: str
    expirationMonth: int
    expirationYear: int
    cvc: int
    