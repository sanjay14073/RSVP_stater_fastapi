from models.User import User, Login
from utils.Authutils import hash_password, verify_password, create_access_token, is_admin
from sqlmodel import select

def signup(new_user: User, session):
    try:
        existing_user = session.exec(select(User).where(User.email == new_user.email)).first()
        if existing_user is not None:
            raise ValueError("Email already exists")
        
        new_user.password = hash_password(new_user.password)
        session.add(new_user)
        session.commit()
        return {"message": "User created successfully"}
    except Exception as e:
        session.rollback()
        return {"error": str(e)}

def login(user: Login, session):
    try:
        existing_user = session.exec(select(User).where(User.email == user.email)).first()
        if existing_user is None or not verify_password(user.password, existing_user.password):
            raise ValueError("Invalid email or password")

        token = create_access_token({"sub": existing_user.email, "role": existing_user.role})
        return {"message": "Login successful", "access_token": token}
    except Exception as e:
        return {"error": str(e)}

def admin_login(user: Login, session):
    try:
        existing_user = session.exec(select(User).where(User.email == user.email)).first()
        if existing_user is None or not verify_password(user.password, existing_user.password):
            raise ValueError("Invalid email or password")
        if not is_admin(existing_user):
            raise ValueError("User is not an admin")

        token = create_access_token({"sub": existing_user.email, "role": existing_user.role})
        return {"message": "Admin login successful", "access_token": token}
    except Exception as e:
        return {"error": str(e)}
