from pydantic import BaseModel

class CreateProductDto(BaseModel):
    merchant_id: int
    product_name: str
    price: float
    quantity: int