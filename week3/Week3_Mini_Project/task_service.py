from models import Task
from logger import logger
tasks_db = [] # In-memory storage for our tasks

class TaskNotFound(Exception): # Custom exceptions for better error handling
    pass
class DuplicateTaskID(Exception):
    pass
def create_task(task: Task):
    try:
        # Check if ID already exists
        for t in tasks_db:
            if t.id == task.id:
                raise DuplicateTaskID(f"Task ID {task.id} already exists!")
        
        tasks_db.append(task)
        logger.info(f"Task created: {task.title}")
        return task
    except DuplicateTaskID as e:
        logger.error(f"Duplicate task ID: {task.id}")
        raise e

def get_all_tasks(completed: bool = None):
    # Query Parameter logic: If 'completed' is provided, filter the list
    if completed is not None:
        filtered_tasks = [t for t in tasks_db if t.completed == completed]
        return filtered_tasks
  
    return tasks_db # Otherwise, return all tasks

def get_task_by_id(task_id: int):
    try:
        for t in tasks_db:
            if t.id == task_id:
                return t
        raise TaskNotFound(f"Task ID {task_id} not found!")
    except TaskNotFound as e:
        logger.error(f"Task not found: ID {task_id}")
        raise e

def update_task(task_id: int, updated_task: Task):
    try:
        for index, t in enumerate(tasks_db):
            if t.id == task_id:
                tasks_db[index] = updated_task
                logger.info(f"Task updated: ID {task_id}")
                return updated_task
        raise TaskNotFound(f"Task ID {task_id} not found!")
    except TaskNotFound as e:
        logger.error(f"Update failed - Task not found: ID {task_id}")
        raise e

def delete_task(task_id: int):
    try:
        for index, t in enumerate(tasks_db):
            if t.id == task_id:
                tasks_db.pop(index)
                logger.info(f"Task deleted: ID {task_id}")
                return {"message": f"Task {task_id} deleted successfully"}
        raise TaskNotFound(f"Task ID {task_id} not found!")
    except TaskNotFound as e:
        logger.error(f"Delete failed - Task not found: ID {task_id}")
        raise e