README.md — FastAPI Task Manager
# 📝 FastAPI Task Manager

A full-stack **Task Management Application** built using **FastAPI** (backend) and **React.js** (frontend).  
It allows users to create, update, delete, and manage tasks efficiently with JWT authentication and RESTful APIs.

---

## 🚀 Features

- ✅ **User Authentication** using JWT (JSON Web Tokens)
- 📋 **CRUD Operations** for tasks (Create, Read, Update, Delete)
- 🗂️ **Organized API Structure** with Routers and Schemas
- 💾 **SQLite Database** using SQLAlchemy ORM
- ⚡ **FastAPI Backend** for high performance and simplicity
- 🌐 **React Frontend** Built a React + JavaScript frontend 



---

## 🧠 Project Structure



task_manager_fastapi/
│
├── main.py # Entry point for FastAPI application
├── auth.py # Handles user authentication (JWT)
├── crud.py # Database CRUD functions
├── database.py # Database configuration (SQLite + SQLAlchemy)
├── models.py # Database models
├── routers/ # Contains API routes
├── schemas.py # Pydantic models for request/response
├── task-manager-frontend/ # React.js frontend code
├── tasks.db # SQLite database file
└── .gitignore # Ignored files and folders


---

## ⚙️ Setup & Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Seban007/task-manager-fastapi.git
cd task-manager-fastapi

2️⃣ Create a Virtual Environment
python -m venv venv
venv\Scripts\activate   # (On Windows)

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the FastAPI Server
uvicorn main:app --reload


👉 The app will run at: http://127.0.0.1:8000

5️⃣ Open the Interactive API Docs

Go to: http://127.0.0.1:8000/docs

You can test all API endpoints from here.

🧩 API Endpoints
Method	Endpoint	Description
POST	/auth/login	User login (JWT authentication)
GET	/tasks/	Fetch all tasks
POST	/tasks/	Create a new task
PUT	/tasks/{id}	Update a task
DELETE	/tasks/{id}	Delete a task
🧰 Tech Stack

Backend: FastAPI, Python, SQLAlchemy, SQLite
Frontend: React.js, JavaScript
Authentication: JWT
Environment: Virtualenv
Version Control: Git & GitHub

👨‍💻 Author

Andrew Sebi Varghese
GitHub: Seban007

🛡️ License

This project is open-source and available under the MIT License
