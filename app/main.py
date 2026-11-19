from fastapi import FastAPI
from pydantic import BaseModel, Field

from app.database import get_connection, init_db

init_db()

app = FastAPI(title="Order Processing System")


class OrderCreate(BaseModel):
    customer_name: str = Field(min_length=1, max_length=50)
    product: str = Field(min_length=1)
    quantity: int = Field(gt=0, le=100)


@app.get("/")
def root():
    return {"message": "Welcome to the Order Processing System"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/orders", status_code=201)
def create_order(order: OrderCreate):
    with get_connection() as conn:
        cursor = conn.execute(
            "INSERT INTO orders (customer_name, product, quantity) VALUES (?, ?, ?)",
            (order.customer_name, order.product, order.quantity),
        )
        row = conn.execute("SELECT * FROM orders WHERE id = ?", (cursor.lastrowid,)).fetchone()
    return dict(row)



@app.get("/orders")
def list_orders():
    with get_connection() as conn:
        rows = conn.execute("SELECT * FROM orders ORDER BY id").fetchall()
    return [dict(row) for row in rows]