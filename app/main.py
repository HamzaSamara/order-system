from fastapi import FastAPI

app = FastAPI(title="Order Processing System New")


@app.get("/")
def root():
    return {"message": "Welcome to the Order Processing System"}


@app.get("/health")
def health():
    return {"status": "ok"}
