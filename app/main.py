from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import get_db, init_db
from app.models import Order

init_db()

app = FastAPI(title="Order Processing System")


class OrderCreate(BaseModel):
    customer_name: str = Field(min_length=1, max_length=50)
    product: str = Field(min_length=1)
    quantity: int = Field(gt=0, le=100)


def order_to_dict(order):
    return {
        "id": order.id,
        "customer_name": order.customer_name,
        "product": order.product,
        "quantity": order.quantity,
        "status": order.status,
        "created_at": order.created_at,
    }



@app.get("/")
def root():
    return {"message": "Welcome to the Order Processing System"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/orders", status_code=201)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    new_order = Order(
        customer_name = order.customer_name,
        product = order.product,
        quantity = order.quantity
    )
    db.add(new_order)
    db.commit()
    return order_to_dict(new_order)


@app.get("/orders")
def list_orders(db: Session = Depends(get_db)):
    orders = db.execute(select(Order).order_by(Order.id)).scalars().all()
    result = []
    for i in orders:
        result.append(order_to_dict(i))
    return result



@app.get("/orders/{order_id}")
def get_order(order_id: int, db: Session = Depends(get_db)):
    order = db.get(Order, order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order_to_dict(order)


