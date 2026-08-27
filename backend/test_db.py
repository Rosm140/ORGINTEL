from sqlalchemy import text

from database import SessionLocal


def test_connection():
    session = SessionLocal()
    try:
        result = session.execute(text("SELECT 1"))
        value = result.scalar()
        print("Database session successful")
        print(f"Result: {value}")
    finally:
        session.close()


if __name__ == "__main__":
    test_connection()
