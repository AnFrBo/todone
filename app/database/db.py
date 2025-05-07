from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config import DATABASE_URL
from app.database.base import Base
from app.database.model import *

# Create engine
engine = create_engine(DATABASE_URL, echo=True)

# Session Factory
SessionLocal = sessionmaker(bind=engine)

# Initialize DB (create tables)
def init_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    print(Base.metadata.tables.keys())

# Session Context Manager (recommended for clean handling)
@contextmanager
def get_session():
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
