from fastapi import FastAPI
from pydantic import BaseModel, Field
from fastapi import FastAPI, HTTPException

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



@app.get("/orders/{order_id}")
def get_order(order_id: int):
    with get_connection() as conn:
        row = conn.execute('select * from orders where id = ?', (order_id,)).fetchone()
    if row is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return dict(row)