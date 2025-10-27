from dataclasses import dataclass


@dataclass
class User:
    name: str
    email: str
    phone_number: str
    id: int = None
