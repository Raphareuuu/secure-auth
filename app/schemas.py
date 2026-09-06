from datetime import datetime

from pydantic import BaseModel, EmailStr, ConfigDict

class RegisterRequest(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    email: EmailStr
    created_at: datetime