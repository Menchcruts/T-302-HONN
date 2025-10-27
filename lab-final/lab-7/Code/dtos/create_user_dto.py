from pydantic import BaseModel

class CreateUserDto(BaseModel):
    name: str
    email: str
    phone_number: str
