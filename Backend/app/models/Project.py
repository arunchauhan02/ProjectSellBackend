from typing import List
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class Project(BaseModel):
    id: Optional[str]
    title: str
    description: str
    tech_stack: List[str]
    difficulty: str
    url: str
    createdAt: datetime=datetime.utcnow()
    fileUrl:str
    public_id:str
    category: str
    price: int
    rating:float = 0.0
    noOfReviews:int = 0