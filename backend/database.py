from sqlalchemy import create_engine

USERNAME = "orgintel"
PASSWORD = "orgintel_dev"
HOST = "localhost"
PORT = 5432
DATABASE = "orgintel"

DATABASE_URL = f"postgresql+psycopg://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"

engine = create_engine(DATABASE_URL)
