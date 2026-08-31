from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from database import SessionLocal
from models import Decision
from schemas import DecisionCreate, DecisionResponse

app = FastAPI()


@app.get("/")
def root():
    return {"message": "ORGINTEL API is running"}


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@app.post("/decisions", response_model=DecisionResponse)
def create_decision(
    decision: DecisionCreate,
    db: Session = Depends(get_db),
):
    db_decision = Decision(
        title=decision.title,
        description=decision.description,
        owner=decision.owner,
        deadline=decision.deadline,
        status=decision.status,
    )

    db.add(db_decision)
    db.commit()
    db.refresh(db_decision)

    return db_decision


@app.get("/decisions", response_model=list[DecisionResponse])
def get_decisions(db: Session = Depends(get_db)):
    return db.query(Decision).all()