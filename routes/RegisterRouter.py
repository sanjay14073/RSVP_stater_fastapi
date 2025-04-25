from fastapi import APIRouter, Depends
from sqlmodel import Session
from typing import List
from db import get_session
from models.Register import Register
from controllers.RegisterContoller import create_register, get_register_by_userid, get_register_by_eventid

router = APIRouter(prefix="/register", tags=["Register"])

@router.post("/", response_model=Register)
def create_register_route(register: Register, session: Session = Depends(get_session)):
    return create_register(register, session)

@router.get("/user/{user_id}", response_model=List[Register])
def get_register_by_userid_route(user_id: str, session: Session = Depends(get_session)):
    return get_register_by_userid(user_id, session)

@router.get("/event/{event_id}", response_model=List[Register])
def get_register_by_eventid_route(event_id: str, session:Session = Depends(get_session)):
    return get_register_by_eventid(event_id, session)

