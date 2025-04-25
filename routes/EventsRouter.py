from fastapi import APIRouter, Depends
from sqlmodel import Session
from typing import List
from datetime import date
from models.Events import Events
from controllers.EventContoller import (
    create_event, get_event, update_event, delete_event,
    get_all_events, get_event_by_name, get_event_by_date, get_event_by_location
)
from db import get_session

router = APIRouter(prefix="/events", tags=["Events"])

@router.post("/", response_model=Events)
def create_event_route(event: Events, session: Session = Depends(get_session)):
    return create_event(event, session)

@router.get("/{event_id}", response_model=Events)
def get_event_route(event_id: int, session: Session = Depends(get_session)):
    return get_event(event_id, session)

@router.put("/{event_id}", response_model=Events)
def update_event_route(event_id: int, event: Events, session: Session = Depends(get_session)):
    return update_event(event_id, event, session)

@router.delete("/{event_id}", response_model=dict)
def delete_event_route(event_id: int, session: Session = Depends(get_session)):
    return delete_event(event_id, session)

@router.get("/", response_model=List[Events])
def get_all_events_route(session: Session = Depends(get_session)):
    return get_all_events(session)

@router.get("/name/{event_name}", response_model=List[Events])
def get_event_by_name_route(event_name: str, session: Session = Depends(get_session)):
    return get_event_by_name(event_name, session)

@router.get("/date/{event_date}", response_model=List[Events])
def get_event_by_date_route(event_date: date, session: Session = Depends(get_session)):
    return get_event_by_date(event_date, session)

@router.get("/location/{event_location}", response_model=List[Events])
def get_event_by_location_route(event_location: str, session: Session = Depends(get_session)):
    return get_event_by_location(event_location, session)

