from dataclasses import dataclass


@dataclass
class MerchantInputModel:
    name: str
    ssn: str
    email: str
    phoneNumber: str
    allowsDiscount: bool
