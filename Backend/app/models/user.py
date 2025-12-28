from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class User(BaseModel):
    id: Optional[str]
    name: str
    email: EmailStr
    password: str
    role: str="student"
    isVerified:bool=False
    createdAt:datetime = datetime.utcnow()