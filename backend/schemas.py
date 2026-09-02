from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class DecisionCreate(BaseModel):
    title: str = Field(min_length=1, max_length=400)
    description: str = Field(min_length=1)
    owner: str = Field(min_length=1, max_length=200)
    deadline: datetime | None = None
    status: str = Field(default="pending", min_length=1, max_length=50)


class DecisionResponse(DecisionCreate):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)