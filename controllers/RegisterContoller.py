from models.Register import Register
from sqlmodel import select

def create_register(register: Register, session):
    try:
        existing_register = session.exec(
            select(Register).where(Register.eventid == register.eventid, Register.userid == register.userid)
        ).first()
        if existing_register is not None:
            raise ValueError("Register entry already exists")
        session.add(register)
        session.commit()
        return {"message": "Register entry created successfully"}
    except Exception as e:
        session.rollback()
        return {"error": str(e)}

def get_register_by_userid(user_id: str, session):
    try:
        register = session.exec(
            select(Register).where(Register.userid == user_id)
        ).all()
        if not register:
            raise ValueError("Register entry for the user not found")
        return register
    except Exception as e:
        return {"error": str(e)}

def get_register_by_eventid(event_id: str, session):
    try:
        register = session.exec(
            select(Register).where(Register.eventid == event_id)
        ).all()
        if not register:
            raise ValueError("Register entry for the event not found")
        return register
    except Exception as e:
        return {"error": str(e)}
