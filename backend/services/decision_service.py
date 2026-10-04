from sqlalchemy.orm import Session

from models import Decision
from schemas import DecisionCreate


def create_decision(
    db: Session,
    decision: DecisionCreate,
) -> Decision:
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

def get_decisions(
    db: Session,
    status: str | None = None,
    skip: int = 0,
    limit: int = 10,
) -> list[Decision]:
    query = db.query(Decision)

    if status:
        query = query.filter(Decision.status == status)

    query = query.offset(skip).limit(limit)

    return query.all()

def update_decision(
    db: Session,
    decision_id: int,
    decision: DecisionCreate,
) -> Decision | None:
    db_decision = (
        db.query(Decision)
        .filter(Decision.id == decision_id)
        .first()
    )

    if db_decision is None:
        return None

    db_decision.title = decision.title
    db_decision.description = decision.description
    db_decision.owner = decision.owner
    db_decision.deadline = decision.deadline
    db_decision.status = decision.status

    db.commit()
    db.refresh(db_decision)

    return db_decision

def delete_decision(
    db: Session,
    decision_id: int,
) -> bool:
    db_decision = (
        db.query(Decision)
        .filter(Decision.id == decision_id)
        .first()
    )

    if db_decision is None:
        return False

    db.delete(db_decision)
    db.commit()

    return True