from dataclasses import dataclass


@dataclass
class BuyerInputModel:
    name: str
    ssn: str
    email: str
    phoneNumber: str