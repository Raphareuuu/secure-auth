from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from ..auth import hash_password
from ..database import get_db
from ..models import User
from ..schemas import RegisterRequest, UserResponse

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register", response_model=UserResponse)
def register(
    user_data: RegisterRequest,
    db: Session = Depends(get_db)
):
    password_hash = hash_password(user_data.password)

    user = User(
        name=user_data.name,
        email=user_data.email,
        password_hash=password_hash
    )

    db.add(user)

    try:
        db.commit()
    except IntegrityError:
        db.rollback()

        raise HTTPException(
            status_code=409,
            detail="E-mail já cadastrado!"
        )
    
    db.refresh(user)

    return user