from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from dependencies import get_db
from models import Decision
from schemas import DecisionCreate, DecisionResponse
from services.decision_service import create_decision


router = APIRouter(
    prefix="/decisions",
    tags=["Decisions"],
)

@router.post("/", response_model=DecisionResponse)
def create_decision_route(
    decision: DecisionCreate,
    db: Session = Depends(get_db),
):
    return create_decision(
        db=db,
        decision=decision,
    )


@router.get("/", response_model=list[DecisionResponse])
def get_decisions(
    status: str | None = None,
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
):
    query = db.query(Decision)

    if status:
        query = query.filter(Decision.status == status)

    query = query.offset(skip).limit(limit)

    return query.all()


@router.put("/{decision_id}", response_model=DecisionResponse)
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


@router.delete("/{decision_id}")
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
