# creating a json file with student information
import json
# list of 3 students
students = [
    {"name": "Garima", "age": 20, "course": "Computer Science"},
    {"name": "Srushti", "age": 21, "course": "Information Technology"},
    {"name": "Neha", "age": 19, "course": "Data Science"}
]
# writing to json file
with open("students.json", "w") as f:
    json.dump(students, f, indent=4)  
print("students.json created!")
print("Total students saved:", len(students))