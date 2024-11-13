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

# Function to create JWT token with an expiration time
def create_access_token(data: dict):
    # Copy the provided data to avoid modifying the original
    to_encode = data.copy()
    # Set the token expiration time
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    # Add the expiration time to the token payload
    to_encode.update({"exp": expire})
    # Encode the token with the secret key and algorithm
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


# Function to check if user exists in the database
def authenticate_user(form_data: OAuth2PasswordRequestForm = Depends()):
    username = form_data.username
    password = form_data.password
    if users_db.get(username) == password:
        return {"username": username}
    raise HTTPException(status_code=401, detail="Incorrect username or password")


# TODO: Implement the login endpoint:
# 1. Create an endpoint with a POST method at "/login" and set the response model to Token.
@app.post("/login", response_model=Token)
# 2. Use OAuth2PasswordRequestForm to validate the form data.
async def login(form_data : OAuth2PasswordRequestForm = Depends()):
# 3. Authenticate the user using the provided form data.
    auth = authenticate_user(form_data)
# 4. Create an access token with the user's username as the subject.
    token = create_access_token(data={"sub":auth["username"]})
# 5. Return the access_token and set the token_type to "bearer".
    return {"access_token":token, "token_type":"bearer"}