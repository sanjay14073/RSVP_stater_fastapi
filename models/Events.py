from uuid import UUID, uuid4
from sqlmodel import SQLModel, Field, Column, DateTime
from sqlalchemy import func
from typing import Optional
from datetime import datetime

class Events(SQLModel, table=True):
    __tablename__ = "events"

    id: UUID = Field(default_factory=uuid4, primary_key=True)

    name: str = Field(
        ..., 
        min_length=3, 
        max_length=50,
        sa_column=Column("name", unique=True)
    )

    description: Optional[str] = None
    date: datetime = Field(...)
    location: str = Field(..., min_length=3, max_length=100)
    
    created_at: datetime = Field(default_factory=datetime.utcnow)
    
    updated_at: Optional[datetime] = Field(
        default=None,
        sa_column=Column(DateTime(timezone=True), onupdate=func.now())
    )

    created_by: UUID = Field(...)
