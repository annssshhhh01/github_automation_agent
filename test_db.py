from sqlalchemy import text

from src.database.session import engine

with engine.connect() as conn:
    result = conn.execute(text("SELECT 1"))
    print(result.scalar())
