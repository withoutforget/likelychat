from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass(slots=True)
class UserModel:
    id: UUID
    username: str
    password: str
    created_at: datetime
    updated_at: datetime
