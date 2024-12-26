import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_DIR = os.path.join(os.path.dirname(__file__), "data")
os.makedirs(DATABASE_DIR, exist_ok=True)

DATABASE_URL = f"sqlite:///{os.path.join(DATABASE_DIR, 'todo.db')}"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()


def create_tables():
    from models import Base
    Base.metadata.create_all(bind=engine)