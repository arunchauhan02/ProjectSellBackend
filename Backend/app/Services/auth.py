from app.repositories.user_repo import get_user_by_email,create_user
from app.models.user import User
from app.core.security import hash_password, verify_password, create_access_token
from fastapi import HTTPException, status

def register_user(user: User):
    existing_user = get_user_by_email(user.email)

    if(existing_user):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
        
    hashed_pwd = hash_password(user.password)

    user_dict = {
        "name":user.name,
        "email":user.email,
        "password":hashed_pwd,
        "role":"student"
    }

    return create_user(user_dict)


def login_user(email:str, password:str):
    user = get_user_by_email(email)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )
    
    if not verify_password(password,user["password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    token = create_access_token({
        "sub":str(user["_id"]),
        "email":user["email"],
        "role":user["role"]
    })

    return {
        "access_token":token,
        "token_type":"bearer"
    }
