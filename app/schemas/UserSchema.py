from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    username: str = Field(..., example="johndoe")
    email: EmailStr = Field(..., example="johndoe@example.com")
    password: str = Field(..., min_length=8, example="secret")

class UserRead(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        from_attributes = True


class UserToken(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user_info: UserRead
