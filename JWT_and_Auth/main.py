from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


app = FastAPI()

Oauth2 = OAuth2PasswordBearer(tokenUrl = "token")

# once post ile token yolluyoruz sisteme ardindan korunan ana sayfaya gidiyoruz 
# cunku once erisim almamiz gerekli izin almamiz gerekli token linkinden

@app.post("/vip-token")
async def vip_token(vip_data: OAuth2PasswordRequestForm = Depends()):
    return {"access_token": vip_data.username+"6969"}

@app.get("/vip-section")
async def vip_section(token: str= Depends(Oauth2)):
    return {"the_token": token}
