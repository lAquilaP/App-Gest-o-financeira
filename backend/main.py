from fastapi import FastAPI

from app.routes.users import router as users_router
from app.routes.auth import router as auth_router

app = FastAPI(
    title="Controle Financeiro API",
    version="1.0.0"
)

app.include_router(users_router)
app.include_router(auth_router)


@app.get("/")
def home():
    return {
        "message": "API funcionando 🚀"
    }