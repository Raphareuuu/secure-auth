#importa fastapi para o projeto
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    email: str
    password: str

@app.get("/")
def home():
    return {"message": "SecureAuth API está funcionando!"}

@app.post("/register")
def register(user: User):
    return{
        "messagem": "Usuário recebido!",
        "name": user.name,
        "email": user.email
    }