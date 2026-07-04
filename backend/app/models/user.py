from enum import Enum
from app.models.base_model import BaseModel
from sqlalchemy import Enum as SqlEnum, String
from sqlalchemy.orm import Mapped, mapped_column

from app.enums.user_role import UserRole
from typing import TYPE_CHECKING
from sqlalchemy.orm import relationship

if TYPE_CHECKING:
    from app.models.transaction import Transaction



class User(BaseModel):
    __tablename__ = "users"

    name: Mapped[str] = mapped_column(String(100), nullable=False)

    email: Mapped[str] = mapped_column(
        String(150),
        unique=True,
        nullable=False,
        index=True
    )

    password_hash: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    role: Mapped[UserRole] = mapped_column(
        SqlEnum(UserRole),
        default=UserRole.USER,
        nullable=False
    )

  