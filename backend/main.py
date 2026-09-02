from fastapi import Depends, FastAPI, HTTPException
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
def get_decisions(
    status: str | None = None,
    db: Session = Depends(get_db),
):
    query = db.query(Decision)

    if status:
        query = query.filter(Decision.status == status)

    return query.all()

@app.put("/decisions/{decision_id}", response_model=DecisionResponse)
def update_decision(
    decision_id: int,
    decision: DecisionCreate,
    db: Session = Depends(get_db),
):
    db_decision = (
        db.query(Decision)
        .filter(Decision.id == decision_id)
        .first()
    )

    if db_decision is None:
        raise HTTPException(
            status_code=404,
            detail="Decision not found",
        )

    db_decision.title = decision.title
    db_decision.description = decision.description
    db_decision.owner = decision.owner
    db_decision.deadline = decision.deadline
    db_decision.status = decision.status

    db.commit()
    db.refresh(db_decision)

    return db_decision

@app.delete("/decisions/{decision_id}")
def delete_decision(
    decision_id: int,
    db: Session = Depends(get_db),
):
    db_decision = (
        db.query(Decision)
        .filter(Decision.id == decision_id)
        .first()
    )

    if db_decision is None:
        raise HTTPException(
            status_code=404,
            detail="Decision not found",
        )

    db.delete(db_decision)
    db.commit()

    return {
        "message": "Decision deleted successfully",
        "id": decision_id,
    }