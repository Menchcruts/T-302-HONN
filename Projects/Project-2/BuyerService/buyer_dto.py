from dataclasses import dataclass


@dataclass
class BuyerDTO:
    name: str
    ssn: str
    email: str
    phoneNumber: str