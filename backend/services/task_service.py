from sqlmodel import Session, select
from typing import List, Optional
from uuid import UUID
import json
from datetime import datetime

import sys
import os

# Add the parent directory to the Python path for Vercel deployment
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from src.models.task import Task, TaskCreate, TaskUpdate, TaskRead
from fastapi import HTTPException, status
from cache.cache_service import cache_service


def json_serializer(obj):
    if isinstance(obj, (UUID, datetime)):
        return str(obj)
    raise TypeError(f"Type {type(obj)} not serializable")


class TaskService:

    @staticmethod
    def create_task(session: Session, task_data: TaskCreate, user_id: UUID) -> TaskRead:
        db_task = Task(**task_data.model_dump(), user_id=user_id) # Unpack all fields from task_data

        session.add(db_task)
        session.commit()
        session.refresh(db_task)

        # invalidate cache
        cache_service.delete(f"user_tasks:{user_id}")

        # Use model_validate to include all fields, converting UUIDs to strings
        task_dict = db_task.model_dump()
        task_dict["id"] = str(task_dict["id"])
        task_dict["user_id"] = str(task_dict["user_id"])
        return TaskRead.model_validate(task_dict)

    @staticmethod
    def get_user_tasks(session: Session, user_id: UUID) -> List[TaskRead]:
        cache_key = f"user_tasks:{user_id}"

        cached = cache_service.get(cache_key)
        if cached:
            data = json.loads(cached)
            return [TaskRead(**item) for item in data]

        statement = select(Task).where(Task.user_id == user_id)
        tasks = session.exec(statement).all()

        task_reads = []
        for task in tasks:
            task_dict = task.model_dump()
            task_dict["id"] = str(task_dict["id"])
            task_dict["user_id"] = str(task_dict["user_id"])
            task_reads.append(TaskRead.model_validate(task_dict))

        cache_service.set(
            cache_key,
            json.dumps(
                [task.model_dump() for task in task_reads],
                default=json_serializer,
            ),
            expire=600,
        )

        return task_reads

    @staticmethod
    def get_task_by_id(
        session: Session, task_id: UUID, user_id: UUID
    ) -> Optional[TaskRead]:

        cache_key = f"task:{task_id}:{user_id}"
        cached = cache_service.get(cache_key)

        if cached:
            return TaskRead(**json.loads(cached))

        statement = select(Task).where(
            Task.id == task_id,
            Task.user_id == user_id,
        )
        task = session.exec(statement).first()

        if not task:
            return None

        # Use model_validate to include all fields, converting UUIDs to strings
        task_dict = task.model_dump()
        task_dict["id"] = str(task_dict["id"])
        task_dict["user_id"] = str(task_dict["user_id"])
        task_read = TaskRead.model_validate(task_dict)

        cache_service.set(
            cache_key,
            json.dumps(task_read.model_dump(), default=json_serializer),
            expire=600,
        )

        return task_read

    @staticmethod
    def update_task(
        session: Session,
        task_id: UUID,
        task_data: TaskUpdate,
        user_id: UUID,
    ) -> Optional[TaskRead]:

        statement = select(Task).where(
            Task.id == task_id,
            Task.user_id == user_id,
        )
        task = session.exec(statement).first()

        if not task:
            return None

        # Apply updates from task_data
        for field, value in task_data.model_dump(exclude_unset=True).items():
            setattr(task, field, value)

        task.updated_at = datetime.utcnow() # Update timestamp

        session.add(task) # Stage changes
        session.commit() # Commit changes to DB
        session.refresh(task) # Refresh to get latest data from DB

        cache_service.delete(f"task:{task_id}:{user_id}")
        cache_service.delete(f"user_tasks:{user_id}")

        # Use model_validate to include all fields, converting UUIDs to strings
        task_dict = task.model_dump()
        task_dict["id"] = str(task_dict["id"])
        task_dict["user_id"] = str(task_dict["user_id"])
        return TaskRead.model_validate(task_dict)

    @staticmethod
    def delete_task(session: Session, task_id: UUID, user_id: UUID) -> bool:
        statement = select(Task).where(
            Task.id == task_id,
            Task.user_id == user_id,
        )
        task = session.exec(statement).first()

        if not task:
            return False

        session.delete(task)
        session.commit()

        cache_service.delete(f"task:{task_id}:{user_id}")
        cache_service.delete(f"user_tasks:{user_id}")

        return True

    @staticmethod
    def toggle_task_completion(
        session: Session, task_id: UUID, user_id: UUID
    ) -> Optional[TaskRead]:

        statement = select(Task).where(
            Task.id == task_id,
            Task.user_id == user_id,
        )
        task = session.exec(statement).first()

        if not task:
            return None

        task.completed = not task.completed
        task.updated_at = datetime.utcnow()

        session.add(task)
        session.commit()
        session.refresh(task)

        cache_service.delete(f"task:{task_id}:{user_id}")
        cache_service.delete(f"user_tasks:{user_id}")

        # Use model_validate to include all fields, converting UUIDs to strings
        task_dict = task.model_dump()
        task_dict["id"] = str(task_dict["id"])
        task_dict["user_id"] = str(task_dict["user_id"])
        return TaskRead.model_validate(task_dict)
