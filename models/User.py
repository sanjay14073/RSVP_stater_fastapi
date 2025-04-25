from typing import Optional
from datetime import datetime
from uuid import uuid4, UUID
from sqlmodel import SQLModel, Field, Column, func, DateTime
from pydantic import EmailStr

class User(SQLModel, table=True):
    __tablename__ = "users"

    id: UUID = Field(default_factory=uuid4, primary_key=True)
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(...)
    full_name: Optional[str] = None
    role: str = Field(default="user", min_length=3, max_length=50)
    
    dob: Optional[datetime] = None

    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(
        default=None,
        sa_column=Column(DateTime(timezone=True), onupdate=func.now())
    )

class Login(SQLModel, table=False):
    email: EmailStr
    password: str = Field(...)

