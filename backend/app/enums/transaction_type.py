from enum import Enum


class TransactionType(str, Enum):
    RECEITA = "RECEITA"
    DESPESA = "DESPESA"