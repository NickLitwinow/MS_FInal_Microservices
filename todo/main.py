from fastapi import FastAPI, HTTPException
from typing import List, Optional
from pydantic import BaseModel
from database import get_db, create_tables
import models

app = FastAPI(
    title="TODO Service",
    description="Сервис для управления списком задач (CRUD).",
    version="1.0.0"
)

create_tables()


class TodoCreate(BaseModel):
    title: str
    description: Optional[str] = None

class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

class TodoOut(BaseModel):
    id: int
    title: str
    description: Optional[str]
    completed: bool

    class Config:
        orm_mode = True


@app.post("/items", response_model=TodoOut)
def create_item(todo_data: TodoCreate):
    db = get_db()
    new_todo = models.Todo(
        title=todo_data.title,
        description=todo_data.description or "",
        completed=False
    )
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo


@app.get("/items", response_model=List[TodoOut])
def get_items():
    db = get_db()
    todos = db.query(models.Todo).all()
    return todos


@app.get("/items/{item_id}", response_model=TodoOut)
def get_item(item_id: int):
    db = get_db()
    todo = db.query(models.Todo).filter(models.Todo.id == item_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Item not found")
    return todo


@app.put("/items/{item_id}", response_model=TodoOut)
def update_item(item_id: int, todo_data: TodoUpdate):
    db = get_db()
    todo = db.query(models.Todo).filter(models.Todo.id == item_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Item not found")

    if todo_data.title is not None:
        todo.title = todo_data.title
    if todo_data.description is not None:
        todo.description = todo_data.description
    if todo_data.completed is not None:
        todo.completed = todo_data.completed

    db.commit()
    db.refresh(todo)
    return todo


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    db = get_db()
    todo = db.query(models.Todo).filter(models.Todo.id == item_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Item not found")

    db.delete(todo)
    db.commit()
    return {"detail": f"Item with id={item_id} was deleted."}