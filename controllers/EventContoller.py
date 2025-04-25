from models.Events import Events

from sqlmodel import select

def create_event(event: Events, session):
    try:
        existing_event = session.exec(
            select(Events).where(Events.name == event.name)
        ).first()
        if existing_event is not None:
            raise ValueError("Event already exists")
        session.add(event)
        session.commit()
        return {"message": "Event created successfully"}
    except Exception as e:
        session.rollback()
        return {"error": str(e)}

def get_event(event_id: str, session):
    try:
        event = session.get(Events, event_id)
        if event is None:
            raise ValueError("Event not found")
        return event
    except Exception as e:
        return {"error": str(e)}

def update_event(event_id: str, event: Events, session):
    try:
        existing_event = session.get(Events, event_id)
        if existing_event is None:
            raise ValueError("Event not found")
        event_data = event.dict(exclude_unset=True)
        for key, value in event_data.items():
            setattr(existing_event, key, value)
        session.add(existing_event)
        session.commit()
        return {"message": "Event updated successfully"}
    except Exception as e:
        session.rollback()
        return {"error": str(e)}

def delete_event(event_id: str, session):
    try:
        event = session.get(Events, event_id)
        if event is None:
            raise ValueError("Event not found")
        session.delete(event)
        session.commit()
        return {"message": "Event deleted successfully"}
    except Exception as e:
        session.rollback()
        return {"error": str(e)}

def get_all_events(session):
    try:
        events = session.exec(select(Events)).all()
        return events
    except Exception as e:
        return {"error": str(e)}

def get_event_by_name(event_name: str, session):
    try:
        event = session.exec(
            select(Events).where(Events.name == event_name)
        ).first()
        if event is None:
            raise ValueError("Event not found")
        return event
    except Exception as e:
        return {"error": str(e)}

def get_event_by_date(event_date: str, session):
    try:
        events = session.exec(
            select(Events).where(Events.date == event_date)
        ).all()
        if not events:
            raise ValueError("Event not found")
        return events
    except Exception as e:
        return {"error": str(e)}

def get_event_by_location(event_location: str, session):
    try:
        events = session.exec(
            select(Events).where(Events.location == event_location)
        ).all()
        if not events:
            raise ValueError("Event not found")
        return events
    except Exception as e:
        return {"error": str(e)}
