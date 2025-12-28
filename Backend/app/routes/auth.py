from fastapi import APIRouter,Depends
from app.Services.auth import register_user,login_user
from app.models.user import User
from datetime import datetime,timedelta
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(prefix = "/auth",tags=["Auth"])

@router.post("/register")
def create_user(user: User):
    return register_user(user)

@router.post("/login")
def login_now(user: OAuth2PasswordRequestForm = Depends()):
    print(user)
    return login_user(user.username,user.password)
