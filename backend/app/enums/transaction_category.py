from enum import Enum


class TransactionCategory(str, Enum):
    ALIMENTACAO = "ALIMENTACAO"
    TRANSPORTE = "TRANSPORTE"
    MORADIA = "MORADIA"
    SAUDE = "SAUDE"
    EDUCACAO = "EDUCACAO"
    LAZER = "LAZER"
    SALARIO = "SALARIO"
    OUTROS = "OUTROS"