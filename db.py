from sqlmodel import SQLModel, create_engine, Session
from typing import Annotated, Generator

# Database setup
sql_lite_file_name = "rsvp.db"
sqlite_url = f"sqlite:///{sql_lite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session
