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