from dataclasses import dataclass


@dataclass
class Buyer:
    name: str
    ssn: str
    email: str
    phoneNumber: str