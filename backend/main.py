
from fastapi import FastAPI

from backend.routes.decisions import router as decisions_router


app = FastAPI()

app.include_router(decisions_router)


@app.get("/")
def root():
    return {"message": "ORGINTEL API is running"}
