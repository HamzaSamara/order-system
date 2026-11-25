import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app.models import Base

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///orders.db")

engine = create_engine(DATABASE_URL)


def init_db():
    Base.metadata.create_all(engine)

def get_db():
    with Session(engine) as session:
        yield session