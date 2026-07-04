from sqlalchemy.orm import Session

from app.models.transaction import Transaction


class TransactionRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, transaction: Transaction):
        self.db.add(transaction)
        self.db.commit()
        self.db.refresh(transaction)
        return transaction

    def get_all_by_user(self, user_id: int):
        return (
            self.db.query(Transaction)
            .filter(Transaction.user_id == user_id)
            .all()
        )

    def get_by_id(self, transaction_id: int):
        return (
            self.db.query(Transaction)
            .filter(Transaction.id == transaction_id)
            .first()
        )

    def delete(self, transaction: Transaction):
        self.db.delete(transaction)
        self.db.commit()