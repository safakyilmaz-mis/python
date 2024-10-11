from typing import Optional
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta
from jose import JWSError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel

SECRET_KEY = ""
ALGORITHM = "SH256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

Token = "b46240f376b977c7c3439f6c42fcbe674237833d687808f4d9a555969f06009a"

fake_database = {
    "username":"safakyilmaz",
    "full_name":"Safak Yilmaz",
    "email": "safakyilmaz@yandex.com",
    "hashed_password": "",
    "disabled": False
}

class Token(BaseModel):
    username: Optional[str] = None
    
class TokenData(BaseModel):
    email : Optional[str] = None
    
class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None
    
class UserInDB(User):
    hashed_password: str
    
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth_2_scheme = OAuth2PasswordBearer(tokenUrl="token")


app = FastAPI()


def verify_pass(plain_pass,hashed_pass):
    return pwd_context.verify(plain_pass,hashed_pass)

def gt_pass_has(password):
    return pwd_context.hash(password)

def get_user(db, username: str):
    if username in db:
        user_data = db[username]
        return UserInDB(**user_data)