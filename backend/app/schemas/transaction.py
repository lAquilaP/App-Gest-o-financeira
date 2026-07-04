from datetime import date, datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict

from app.enums.transaction_category import TransactionCategory
from app.enums.transaction_type import TransactionType


class TransactionCreate(BaseModel):
    description: str
    amount: Decimal
    transaction_date: date
    type: TransactionType
    category: TransactionCategory


class TransactionUpdate(BaseModel):
    description: str | None = None
    amount: Decimal | None = None
    transaction_date: date | None = None
    type: TransactionType | None = None
    category: TransactionCategory | None = None


class TransactionResponse(BaseModel):
    id: int
    description: str
    amount: Decimal
    transaction_date: date
    type: TransactionType
    category: TransactionCategory
    user_id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)