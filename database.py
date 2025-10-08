from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# -----------------------------
# DATABASE URL (SQLite local)
# -----------------------------
SQLALCHEMY_DATABASE_URL = "sqlite:///./task_manager.db"

# -----------------------------
# ENGINE CREATION
# -----------------------------
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# -----------------------------
# SESSIONLOCAL for DB sessions
# -----------------------------
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# -----------------------------
# BASE CLASS for models
# -----------------------------
Base = declarative_base()

# -----------------------------
# DB DEPENDENCY
# -----------------------------
def get_db():
    """
    Dependency that provides a database session to routes.
    It will close automatically after the request.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
