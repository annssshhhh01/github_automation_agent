from sqlmodel import SQLModel, Session, create_engine

from src.config import config

engine = create_engine(
    config.DATABASE_URL,
    echo=True,
    pool_pre_ping=True,
)

def get_session():
    with Session(engine) as session:
        yield session
