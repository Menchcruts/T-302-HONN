from dataclasses import dataclass
@dataclass
class BuyerResponseDTO:
    name: str
    ssn: str
    email: str
    phone_number: str
