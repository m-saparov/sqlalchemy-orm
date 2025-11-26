from .models import Task
from .db import get_db


def create_task(title: str, description: str | None = None):
    task = Task(
        title=title,
        description=description
    )

    with get_db() as session:
        session.add(task)
        session.commit()


def get_tasks() -> list[Task]:
    with get_db() as session:
        tasks = session.query(Task).order_by(Task.id.asc()).all()

    return tasks


def get_one_task(task_id: int) -> Task | None:
    with get_db() as session:
        task = session.query(Task).get(task_id)

    return task


def update_task(
    task_id: int,
    title: str | None = None,
    description: str | None = None
):
    task = get_one_task(task_id)

    if task:
        with get_db() as session:
            task.title = title if title else task.title
            task.description = description if description else task.description

            session.add(task)
            session.commit()

        return task

    return None


def delete_task(task_id: int):
    task = get_one_task(task_id)

    if task:
        with get_db() as session:
            session.delete(task)
            session.commit()

        return True

    return False


def change_task_status(task_id: int):
    task = get_one_task(task_id)

    if task:
        with get_db() as session:
            task.completed = not task.completed
            session.add(task)
            session.commit()

        return task

    return None
