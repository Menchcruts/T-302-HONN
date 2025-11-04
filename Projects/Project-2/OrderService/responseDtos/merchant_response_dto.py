from dataclasses import dataclass


@dataclass
class MerchantResponseDTO:
    name: str
    ssn: str
    email: str
    phone_number: str
    allows_discount: bool
