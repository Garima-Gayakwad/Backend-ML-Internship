# adding a new student to existing students.json
import json
# first read existing data
with open("students.json", "r") as f:
    data = json.load(f)
print("Students before adding:", len(data))
# new student to add
new_student = {"name": "Amit", "age": 22, "course": "AI/ML"}
data.append(new_student)  # adding to the list
# writing back to file
with open("students.json", "w") as f:
    json.dump(data, f, indent=4)
print("New student added!")
print("Students after adding:", len(data))