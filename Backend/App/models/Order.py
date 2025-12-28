class Order(BaseModel):
    id: Optional[str]
    user_id: str
    project_id: str
    amount_paid: float
    payment_status: str
    payment_id: Optional[str]
    purchased_at: datetime= datetime.utcnow()
