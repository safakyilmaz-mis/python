from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from jose import jwt
from datetime import datetime, timedelta

app = FastAPI()

# Mock database with usernames and passwords
users_db = {"user1": "pass1", "user2": "pass2"}

# Configuration for JWT
SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


# TODO: Define the Token class with the necessary fields:
# - access_token (str)
# - token_type (str)
class Token(BaseModel):
    access_token:str
    token_type:str


# TODO: Implement the function to create JWT token with an expiration time:
# - Copy the provided data to avoid modifying the original
# - Set the token expiration time
# - Add the expiration time to the token payload
# - Encode the token with the secret key and algorithm, and return it

def create_access_token(user_data: dict):
    user_data = user_data.copy()
    exp_time = datetime.now() + timedelta(minutes=30)
    user_data.update({"exp":exp_time})
    return jwt.encode(user_data,SECRET_KEY,algorithm=ALGORITHM)

# The authenticate_user function is provided and does not need to be written by the user
def authenticate_user(form_data: OAuth2PasswordRequestForm = Depends()):
    username = form_data.username
    password = form_data.password
    if users_db.get(username) == password:
        return {"username": username}
    raise HTTPException(status_code=401, detail="Incorrect username or password")


# TODO: Implement the login endpoint:
# 1. Create an endpoint with a POST method at "/login" and set the response model to Token.
# 2. Use OAuth2PasswordRequestForm to validate the form data.
# 3. Authenticate the user using the provided form data.
# 4. Create an access token with the user's username as the subject.
# 5. Return the access_token and set the token_type to "bearer".

@app.post("/login",response_model=Token)
async def login(user_data : OAuth2PasswordRequestForm = Depends()):
    auth = authenticate_user(user_data)
    token_create = create_access_token({"sub":auth["username"]})
    return {"access_token":token_create, "token_type":"bearer"}