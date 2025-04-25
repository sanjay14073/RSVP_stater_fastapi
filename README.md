# RSVP Application

A simple RSVP and event registration API built with **FastAPI**, **SQLModel**, and **SQLite**.

---

## Features

- User authentication (signup, login, admin login)
- Event management (create, list events)
- Event registration for users
- Role-based access (user/admin)
- Secure password hashing and JWT token-based authentication

---

## Project Structure

- **main.py** — FastAPI app entry point, includes middleware, CORS, and router inclusion  
- **db.py** (or DB logic inside main.py) — Database connection, session management, and table creation  
- **models/** — SQLModel data models for User, Event, Register, Login  
- **routes/** — API routes organized by feature (AuthRouter, EventsRouter, RegisterRouter)  
- **controllers/** — Business logic and database interactions for each feature (AuthController, RegisterController, EventController)  
- **utils/** — Utilities for authentication (password hashing, JWT token creation, role checks)  

---

## Controllers Overview

### AuthController
- Handles user signup, login, and admin login  
- Checks for existing users, hashes passwords, verifies credentials  
- Generates JWT access tokens with role information  

### RegisterController
- Handles registering a user to an event  
- Fetches registrations by user ID or event ID  
- Ensures relational integrity with foreign keys  

### EventController
- Manages event creation and retrieval  
- Handles event metadata like name, description, date, location, and creator  

---

## Setup & Running

1. Clone the repo  
2. Install dependencies  
   ```bash
   pip install -r requirements.txt
   ```  
3. Run the app  
   ```bash
   uvicorn main:app --reload
   ```  
   or
   ```bash
   fastapi dev main.py
   ```
4. The API will be available at `http://localhost:8000`  
5. Use Swagger UI at `http://localhost:8000/docs` for interactive API testing  

---

Contributions are welcome as this is a starter kit with less features currently.