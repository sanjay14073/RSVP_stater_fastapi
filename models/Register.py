from uuid import uuid4, UUID
from sqlmodel import SQLModel, Field, Column, ForeignKey
from typing import Optional

class Register(SQLModel, table=True):
    __tablename__ = "register"
    
    id: UUID = Field(default_factory=uuid4, primary_key=True)

    eventid: UUID = Field(
        ..., 
        sa_column=Column(ForeignKey("events.id"))
    )

    userid: UUID = Field(
        ..., 
        sa_column=Column(ForeignKey("users.id"))
    )

    
