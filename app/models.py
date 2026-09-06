from datetime import datetime
from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from .database import Base

#Estou criando um modelo chamado User baseado na estrutura que o SQLAlchemy conhece
#A classe User corresponde à tabela users que já existe
class User(Base):
    __tablename__ = "users" #Essa classe representa a tabela users do PostgreSQL

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False) #nullable=False significa que não pode ficar vazio.
    email: Mapped[str] = mapped_column(
        String(255),
        unique=True, #significa que dois usuários não podem possuir o mesmo e-mail.
        nullable=False
    )
    password_hash: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default = datetime.utcnow
    )

