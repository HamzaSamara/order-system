from sqlalchemy import func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    customer_name: Mapped[str]
    product: Mapped[str]
    quantity: Mapped[int]
    status: Mapped[str] = mapped_column(server_default="pending")
    created_at: Mapped[str] = mapped_column(server_default=func.now())