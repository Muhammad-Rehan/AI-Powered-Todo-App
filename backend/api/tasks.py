# src/api/tasks.py
from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlmodel import Session
from typing import List
from uuid import UUID

from services.task_service import TaskService
from src.models.task import TaskCreate, TaskRead, TaskUpdate
from api.dependencies import get_current_user_id, get_db_session

router = APIRouter(tags=["Tasks"])

# -------------------------------
# Get all tasks for current user
# -------------------------------
@router.get("/", response_model=List[TaskRead])
def get_user_tasks(
    current_user_id: UUID = Depends(get_current_user_id),
    session: Session = Depends(get_db_session)
):
    return TaskService.get_user_tasks(session, current_user_id)


# -------------------------------
# Create a new task
# -------------------------------
@router.post("/", response_model=TaskRead, status_code=status.HTTP_201_CREATED)
def create_task(
    task_data: TaskCreate,
    current_user_id: UUID = Depends(get_current_user_id),
    session: Session = Depends(get_db_session)
):
    return TaskService.create_task(session, task_data, current_user_id)


# -------------------------------
# Get a specific task by ID
# -------------------------------
@router.get("/{task_id}", response_model=TaskRead)
def get_task(
    task_id: UUID,
    current_user_id: UUID = Depends(get_current_user_id),
    session: Session = Depends(get_db_session)
):
    task = TaskService.get_task_by_id(session, task_id, current_user_id)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return task


# -------------------------------
# Update a task by ID
# -------------------------------
@router.put("/{task_id}", response_model=TaskRead)
def update_task(
    task_id: UUID,
    task_data: TaskUpdate,
    current_user_id: UUID = Depends(get_current_user_id),
    session: Session = Depends(get_db_session)
):
    task = TaskService.update_task(session, task_id, task_data, current_user_id)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return task


# -------------------------------
# Delete a task by ID
# -------------------------------
@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(
    task_id: UUID,
    current_user_id: UUID = Depends(get_current_user_id),
    session: Session = Depends(get_db_session)
):
    success = TaskService.delete_task(session, task_id, current_user_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# -------------------------------
# Toggle task completion
# -------------------------------
@router.patch("/{task_id}/toggle", response_model=TaskRead)
def toggle_task_completion(
    task_id: UUID,
    current_user_id: UUID = Depends(get_current_user_id),
    session: Session = Depends(get_db_session)
):
    task = TaskService.toggle_task_completion(session, task_id, current_user_id)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return task
