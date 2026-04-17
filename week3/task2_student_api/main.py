from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

# pydantic model - defines what a student looks like
# pydantic automatically validates the data types
class Student(BaseModel):
    id: int
    name: str
    age: int
    course: str

students = [] # storing students in memory

@app.get("/") # GET / - home route
def home():
    return {"message": "Welcome to Garima's Student API"}

@app.post("/students") # POST /students - accepts student data and stores it
def add_student(student: Student):
    # checking if id already exists
    for s in students:
        if s["id"] == student.id:
            return {"error": "student with this ID already exists!"}

    students.append(student.dict())  # converting pydantic model to dict
    return {"message": "Student added!", "student": student}

@app.get("/students") # GET /students - returns all students
def get_students():
    if not students:
        return {"message": "no students yet!"}
    return {"students": students}