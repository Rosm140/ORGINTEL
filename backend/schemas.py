from datetime import datetime
from enum import Enum
from pydantic import BaseModel, ConfigDict, Field

class DecisionStatus(str, Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class DecisionCreate(BaseModel):
    title: str = Field(min_length=1, max_length=400)
    description: str = Field(min_length=1)
    owner: str = Field(min_length=1, max_length=200)
    deadline: datetime | None = None
    status: DecisionStatus = DecisionStatus.PENDING
    
class DecisionResponse(DecisionCreate):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)