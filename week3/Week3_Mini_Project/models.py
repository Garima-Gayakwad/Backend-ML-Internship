from pydantic import BaseModel
# Defines what a valid Task must look like
class Task(BaseModel):
    id: int
    title: str
    description: str
    completed: bool