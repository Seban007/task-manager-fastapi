Task Manager Application (FastAPI + React + JavaScript)
Overview

A full-stack Task Management System built with FastAPI for the backend and React + JavaScript for the frontend. This project allows users to register, log in, and manage tasks (create, read, update, delete) securely using JWT authentication.

Features
Backend (FastAPI)

RESTful API with FastAPI

User authentication with JWT tokens

CRUD operations for tasks

SQLite database using SQLAlchemy ORM

Password hashing with bcrypt

Input validation with Pydantic schemas

CORS enabled for frontend integration

Frontend (React + JavaScript)

Single Page Application (SPA) built with React and vanilla JS

Responsive and interactive UI

User registration and login

Create, edit, delete, and view tasks

Integration with backend REST API

Handles JWT authentication and stores token securely in localStorage

Real-time task updates in the UI

Tech Stack

Backend: Python, FastAPI, SQLAlchemy, SQLite, JWT, Pydantic

Frontend: React, JavaScript, HTML5, CSS3

Tools: Git, GitHub, Uvicorn, Postman/Swagger UI

Installation
Backend
# Clone the repository
git clone https://github.com/Seban007/task-manager-fastapi.git
cd task-manager-fastapi

# Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Run FastAPI server
uvicorn main:app --reload --port 8000

Frontend
# Navigate to frontend folder
cd task-manager-frontend

# Install dependencies
npm install

# Start frontend
npm start


Frontend runs on http://localhost:3000 and connects to backend API.

Usage

Open the frontend in the browser (http://localhost:3000)

Register a new user or login with existing credentials

Use the dashboard to:

Create new tasks

Edit existing tasks

Delete tasks

Mark tasks as completed

All operations are reflected in the backend API and database License

Project Structure
task-manager-fastapi/
│
├── main.py              # FastAPI entry point
├── database.py          # Database setup
├── models.py            # SQLAlchemy models
├── schemas.py           # Pydantic schemas
├── auth.py              # JWT & authentication
├── routers/             # API routes
│   ├── users.py
│   └── tasks.py
├── task-manager-frontend/  # React frontend
│   ├── public/
│   └── src/
└── requirements.txt

Highlights

Full-stack project (React frontend + FastAPI backend)

Secure authentication using JWT tokens

Real-time CRUD functionality

Fully functional and deployable application

Demonstrates ability to build full-stack web applications

