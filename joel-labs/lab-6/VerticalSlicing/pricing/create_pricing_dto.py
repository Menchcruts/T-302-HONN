from pydantic import BaseModel

class CreatePricingDto(BaseModel):
    name: str
    price: float
