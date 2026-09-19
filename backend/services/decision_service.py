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