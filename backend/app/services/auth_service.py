from app.core.security import (
    create_access_token,
    verify_password
)
from app.repositories.user_repository import UserRepository


class AuthService:

    def __init__(
        self,
        repository: UserRepository
    ):
        self.repository = repository

    def login(
        self,
        email: str,
        password: str
    ) -> str:

        user = self.repository.get_by_email(
            email
        )

        if not user:
            raise ValueError(
                "Credenciais inválidas."
            )

        if not verify_password(
            password,
            user.password_hash
        ):
            raise ValueError(
                "Credenciais inválidas."
            )

        return create_access_token(
            {
                "sub": str(user.id)
            }
        )