from datetime import date
from pydantic import BaseModel

class CreateSubscriptionDto(BaseModel):
    start_date: date
    end_date: date
    pricing_id: int
    user_id: int
