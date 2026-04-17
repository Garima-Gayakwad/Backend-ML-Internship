# reading students.json and printing all details
import json
with open("students.json", "r") as f:
    data = json.load(f)  # loads json into a list
print("All student details:")
print("   ")
for s in data:
    print(f"Name   : {s['name']}")
    print(f"Age    : {s['age']}")
    print(f"Course : {s['course']}")
    print("   ")