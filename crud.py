# crud.py
from sqlalchemy.orm import Session
import models, schemas

def create_task(db: Session, task: schemas.TaskCreate, user_id: int):
    db_task = models.Task(title=task.title, description=task.description, completed=task.completed, user_id=user_id)
    db.add(db_task); db.commit(); db.refresh(db_task)
    return db_task

def get_tasks_by_user(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Task).filter(models.Task.user_id == user_id).offset(skip).limit(limit).all()

def get_task(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()

def update_task_full(db: Session, task_id: int, update: schemas.TaskCreate):
    db_task = get_task(db, task_id)
    if db_task:
        db_task.title = update.title
        db_task.description = update.description
        db_task.completed = update.completed
        db.commit(); db.refresh(db_task)
    return db_task

def delete_task(db: Session, task_id: int):
    db_task = get_task(db, task_id)
    if db_task:
        db.delete(db_task); db.commit()

