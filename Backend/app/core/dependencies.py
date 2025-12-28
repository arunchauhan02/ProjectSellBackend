from fastapi import Depends,HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from app.database import db
from bson import ObjectId
import os

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token,os.getenv("SECRET_KEY"),"HS256")
        user_id:str = payload.get("sub")

        if(user_id is None):
            raise HTTPException(status_code=401,detail="Invalid token")
    except JWTError:
        raise HTTPException(status_code=401,detail="Invalid token")
    user = db.users.find_one({"_id":ObjectId(user_id)})
    if not user:
        raise HTTPException(status_code=401,detail="User Not Found")
    return user

def get_current_admin(token:str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token,os.getenv("SECRET_KEY"),"HS256")
        user_id:str = payload.get("sub")
        role = payload.get("role")

        if(role != "admin"):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Admin access only"
            )
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access only"
        )
    admin = db.users.find({"_id":ObjectId(user_id)})
    if not admin:
        raise HTTPException(
            status_code=400,
            detail="Admin not found"
        )
    return admin
