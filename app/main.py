from fastapi import FastAPI

from app.database import init_db

init_db()

app = FastAPI(title="Order Processing System")


@app.get("/")
def root():
    return {"message": "Welcome to the Order Processing System"}


@app.get("/health")
def health():
    return {"status": "ok"}