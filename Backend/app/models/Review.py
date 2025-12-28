class Review(BaseModel):
    id: Optional[str]
    project_id: str
    userName:str
    user_id: str
    rating: int
    comment: Optional[str]
    createdAt: datetime = datetime.utcnow()