from datetime import date
from decimal import Decimal
from enum import Enum
from app.models.base_model import BaseModel
from sqlalchemy import Date, Enum as SqlEnum, ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING
from app.enums.transaction_type import TransactionType
from app.enums.transaction_category import TransactionCategory

if TYPE_CHECKING:
    from app.models.user import User


class Transaction(BaseModel):
    __tablename__ = "transactions"

    description: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    amount: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False
    )

    transaction_date: Mapped[date] = mapped_column(
        Date,
        nullable=False
    )

    type: Mapped[TransactionType] = mapped_column(
        SqlEnum(TransactionType),
        nullable=False
    )

    category: Mapped[TransactionCategory] = mapped_column(
        SqlEnum(TransactionCategory),
        nullable=False
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )

    user: Mapped["User"] = relationship(
        back_populates="transactions"
    )