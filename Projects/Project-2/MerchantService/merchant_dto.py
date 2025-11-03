from dataclasses import dataclass


@dataclass
class MerchantDto:
    name: str
    ssn: str
    email: str
    phoneNumber: str
    allowsDiscount: bool
