from dataclasses import dataclass


@dataclass
class ProductResponseDTO:
    merchantId: int
    productName: str
    price: float
    quantity: int
    reserved: int


