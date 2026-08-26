import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine

ROOT_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = ROOT_DIR / ".env"

load_dotenv(ENV_PATH)

USERNAME = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASSWORD")
HOST = os.getenv("DB_HOST", "localhost")
PORT = os.getenv("DB_PORT", "5432")
DATABASE = os.getenv("DB_NAME")

if not all([USERNAME, PASSWORD, DATABASE]):
    raise ValueError(
        "Missing database environment variables. Check your .env file at the project root."
    )

DATABASE_URL = (
    f"postgresql+psycopg://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
)

engine = create_engine(DATABASE_URL)
