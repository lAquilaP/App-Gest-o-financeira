from app.core.security import hash_password
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate


class UserService:

    def __init__(
        self,
        repository: UserRepository
    ):
        self.repository = repository

    def create(
        self,
        data: UserCreate
    ) -> User:

        exists = self.repository.get_by_email(
            data.email
        )

        if exists:
            raise ValueError(
                "E-mail já cadastrado."
            )

        user = User(
            name=data.name,
            email=data.email,
            password_hash=hash_password(
                data.password
            )
        )

        return self.repository.create(
            user
        )