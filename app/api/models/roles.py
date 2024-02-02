from typing import Optional
from enum import Enum
from pydantic import BaseModel, Field, validator
from datetime import datetime
from uuid import UUID4

class RoleType(str, Enum):
    PLATFORM_ADMIN = 'PLATFORM_ADMIN'
    PLATFORM_USER = 'PLATFORM_USER'
    FREE_USER = 'FREE_USER'
    PRO_USER = 'PRO_USER'
    COMMUNITY_MANAGER = 'COMMUNITY_MANAGER'
    COMMUNITY_EDITOR = 'COMMUNITY_EDITOR'

class Role(BaseModel):
    id: Optional[UUID4] = Field(None, regex="^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$")
    name: str = Field(..., min_length=3)
    type: RoleType
    logoAttachmentId: Optional[UUID4]
    active: bool
    createdAt: Optional[datetime]
    updatedAt: datetime = datetime.now()

    @validator('createdAt', 'updatedAt', pre=True)
    def parse_date(cls, v):
        return datetime.fromisoformat(v)

class RoleResponse(BaseModel):
    id: UUID4
    name: str
    type: RoleType
    logoAttachmentId: Optional[UUID4]
    active: bool
    createdAt: datetime
    updatedAt: datetime

class RoleCreate(BaseModel):
    name: str = Field(..., min_length=3)
    type: RoleType
    createdAt: datetime = datetime.now()

    @validator('createdAt', pre=True)
    def parse_date(cls, v):
        return datetime.fromisoformat(v)