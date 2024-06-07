from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.config import settings

engine = create_engine(settings.SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

SESSIONLOCAL = sessionmaker(autoflush=False, autocommit=False, bind=engine)


def get_db():
    db = SESSIONLOCAL()
    try:
        yield db
    finally:
        db.close()