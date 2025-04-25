from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import AuthRouter as auth, EventsRouter as events, RegisterRouter as register
import uvicorn
from db import create_db_and_tables
# FastAPI app
app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Include routers
app.include_router(auth.router)
app.include_router(events.router)
app.include_router(register.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")


