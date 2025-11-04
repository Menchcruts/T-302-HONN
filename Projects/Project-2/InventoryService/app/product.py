from dataclasses import dataclass

@dataclass
class Product:
    merchant_id: int
    product_name: str
    price: float
    quantity: int
    reserved: int