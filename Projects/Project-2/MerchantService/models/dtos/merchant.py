from dataclasses import dataclass


@dataclass
class MerchantDTO:
    name: str
    ssn: str
    email: str
    phoneNumber: str
    allowsDiscount: bool