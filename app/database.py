import os
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from app.models import Base

DATABASE_PATH = os.getenv("DATABASE_PATH", "orders.db")
DATABASE_URL = f"sqlite:///{DATABASE_PATH}"

engine = create_engine(DATABASE_URL)


def init_db():
    Base.metadata.create_all(engine)

def get_db():
    with Session(engine) as session:
        yield session