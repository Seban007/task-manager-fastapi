Task Manager Application

A full-stack Task Management application with FastAPI backend and React + JavaScript frontend. Manage your tasks efficiently with secure user authentication and real-time CRUD operations.

🚀 Features

Backend (FastAPI):

User registration and login with JWT authentication.

Secure password hashing with bcrypt.

CRUD operations for tasks: Create, Read, Update, Delete.

Task ownership linked to users.

Fully documented API with Swagger UI.

Frontend (React + JS):

Interactive task dashboard with real-time updates.

Add, edit, complete, and delete tasks.

User login and registration forms integrated with backend JWT auth.

Modern, responsive UI for desktop and mobile.

📦 Tech Stack
Layer	Technology
Backend	Python, FastAPI
Frontend	React, JavaScript, CSS
Database	SQLite
Authentication	JWT, OAuth2PasswordBearer
Tools	Uvicorn, SQLAlchemy, Passlib, Swagger UI
⚡ How to Run

Backend:

# Clone repo
git clone https://github.com/Seban007/task-manager-fastapi.git
cd task-manager-fastapi

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Run FastAPI backend
uvicorn main:app --reload --port 9000


Frontend:

cd task-manager-frontend
npm install
npm start


Open http://localhost:3000
 in your browser to use the app.
)

🔑 Usage

Register a new user in Swagger UI or frontend.

Login to obtain JWT token.

Authorize in Swagger UI using JWT to access protected routes.

Use frontend to create, update, complete, or delete tasks.

🎯 Learning Outcome

Hands-on experience with FastAPI backend and React frontend integration.

Implemented secure user authentication with JWT.

Built a responsive and interactive task manager from scratch.

Learned deployment and GitHub repo management.

🔗 Links

Backend Repository: Task Manager FastAPI

👨‍💻 Author

Andrew Sebi Varghese
GitHub: Seban007

🛡️ License

This project is open-source and available under the MIT License.

