from pydantic import BaseModel, EmailStr, Field

class BenefitRead(BaseModel):
    id: int
    name: str