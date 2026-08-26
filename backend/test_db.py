from sqlalchemy import text

from database import engine


def test_connection():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        value = result.scalar()
        print("Database connection successful")
        print(f"Result: {value}")


if __name__ == "__main__":
    test_connection()
