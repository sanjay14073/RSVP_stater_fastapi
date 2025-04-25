from fastapi import APIRouter, Depends
from sqlmodel import Session

from db import get_session
from models.User import User, Login
from controllers.AuthController import signup, login, admin_login

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/signup", response_model=dict)
def signup_route(new_user: User, session: Session = Depends(get_session)):
    return signup(new_user, session)

@router.post("/login", response_model=dict)
def login_route(user: Login, session: Session = Depends(get_session)):
    return login(user, session)

@router.post("/admin-login", response_model=dict)
def admin_login_route(user: Login, session: Session = Depends(get_session)):
    return admin_login(user, session)

