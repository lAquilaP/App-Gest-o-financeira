from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.repositories.user_repository import UserRepository
from app.schemas.auth import TokenResponse
from app.services.auth_service import AuthService

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post(
    "/login",
    response_model=TokenResponse
)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    service = AuthService(
        UserRepository(db)
    )

    try:

        token = service.login(
            form_data.username,   # email
            form_data.password
        )

        return TokenResponse(
            access_token=token
        )

    except ValueError:
        raise HTTPException(
            status_code=401,
            detail="E-mail ou senha inválidos."
        )