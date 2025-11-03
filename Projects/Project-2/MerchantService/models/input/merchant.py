from dataclasses import dataclass


@dataclass
class Merchant:
    name: str
    ssn: str
    email: str
    phoneNumber: str
    allowsDiscout: bool