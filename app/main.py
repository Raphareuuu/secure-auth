#importa fastapi para o projeto
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from .database import get_db
from .models import User
from .auth import hash_password

app = FastAPI()

@app.get("/")
def home():
    return {"message": "SecureAuth API está funcionando!"}

@app.post("/register")
def register(
    name: str,
    email: str,
    password: str,
    db: Session = Depends(get_db)
):
    password_hash = hash_password(password)
    
    user = User(
        name = name,
        email = email,
        password_hash = password_hash
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return{
        "message": "Usuário criado com sucesso!",
        "id": user.id,
        "name": user.name,
        "email": user.email
    }