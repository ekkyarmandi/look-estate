from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from decouple import config

db_url = config("DB_URL")
engine = create_engine(db_url)
SessionLocal = sessionmaker(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
