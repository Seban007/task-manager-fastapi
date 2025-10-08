from pydantic import BaseModel

# -------- Task Schemas --------
class TaskBase(BaseModel):
    title: str
    description: str | None = None

class TaskCreate(TaskBase):
    completed: bool = False

class Task(TaskCreate):
    id: int
    user_id: int | None = None

    class Config:
        from_attributes = True

# -------- User Schemas --------
class UserCreate(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True

# -------- Token Schema --------
class Token(BaseModel):
    access_token: str
    token_type: str

