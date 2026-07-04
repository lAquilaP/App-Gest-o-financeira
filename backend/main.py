from fastapi import FastAPI

app = FastAPI(
    title="Controle Financeiro API",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "API funcionando 🚀"
    }