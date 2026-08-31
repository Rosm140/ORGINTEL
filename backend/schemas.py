from datetime import datetime

from pydantic import BaseModel, ConfigDict


class DecisionCreate(BaseModel):
    title: str
    description: str
    owner: str
    deadline: datetime | None = None
    status: str = "pending"


class DecisionResponse(DecisionCreate):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)