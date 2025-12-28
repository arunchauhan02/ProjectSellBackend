from passlib.context import CryptContext
from datetime import datetime,timedelta
from jose import jwt
import os

pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")

def hash_password(password:str)->str:
    return pwd_context.hash(password)

def verify_password(password: str,hash_password:str)->bool:
    return pwd_context.verify(password,hash_password)

def create_access_token(data: dict):
    to_encode = data.copy() 
    expire = datetime.utcnow()+timedelta(minutes=900)

    to_encode.update({"exp":expire})
    return jwt.encode(to_encode,os.getenv("SECRET_KEY"),algorithm="HS256")
