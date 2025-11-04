from dataclasses import dataclass


@dataclass
class ProductResponseDTO:
    merchant_id: int
    product_name: str
    price: float
    quantity: int
    reserved: int


