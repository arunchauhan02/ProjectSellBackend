from app.database import db

def get_user_by_email(email: str):
    return db.users.find_one({"email":email})

def create_user(user_data: dict):
    db.users.insert_one(user_data)
    return {"message":"User Registered successfully"}
