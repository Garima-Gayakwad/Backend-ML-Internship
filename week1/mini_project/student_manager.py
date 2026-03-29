import json
import os
# this is the file where all student data will be saved
FILE = "miniproject_students.json"

# loading students from file, if file doesnt exist return empty list
def load_students():
    if os.path.exists(FILE):
        f = open(FILE, "r")
        data = json.load(f)
        f.close()
        return data
    return []  # no file yet, so empty list
# saving students list back to the file
def save_students(students):
    f = open(FILE, "w")
    json.dump(students, f, indent=4)
    f.close()
# adding a new student
def add_student():
    students = load_students()
    print("\nAdd Student-  ")
    # getting student id
    sid = input("Enter Student ID: ").strip()
    if sid == "":
        print("ID cannot be empty!")
        return
    # checking if id already exists
    for s in students:
        if s["id"] == sid:
            print("This ID already exists! ID must be unique.")
            return
    # getting name
    name = input("Enter Name: ").strip()
    if name == "":
        print("Name cannot be empty!")
        return
    # getting age - must be a number
    age = input("Enter Age: ").strip()
    if not age.isdigit():
        print("Age must be a number!")
        return

    course = input("Enter Course: ").strip()
    # creating student dictionary
    student = {
        "id": sid,
        "name": name,
        "age": int(age),
        "course": course
    }
    students.append(student)  # adding to list
    save_students(students)   # saving to file
    print(f"\nStudent {name} added successfully!")

# viewing all students
def view_students():
    students = load_students()
    print("\nAll Students-  ")
    if len(students) == 0:
        print("No students found!")
        return
    for s in students:
        print(f"ID: {s['id']} | Name: {s['name']} | Age: {s['age']} | Course: {s['course']}")

# searching student by id
def search_student():
    students = load_students()
    print("\nSearch Student-  ")
    sid = input("Enter Student ID to search: ").strip()
    found = False
    for s in students:
        if s["id"] == sid:
            print(f"\nStudent Found!")
            print(f"ID     : {s['id']}")
            print(f"Name   : {s['name']}")
            print(f"Age    : {s['age']}")
            print(f"Course : {s['course']}")
            found = True
            break
    if not found:
        print("No student found with this ID!")

# updating student details by id
def update_student():
    students = load_students()
    print("\nUpdate Student-  ")
    sid = input("Enter Student ID to update: ").strip()

    for s in students:
        if s["id"] == sid:
            print(f"Found: {s['name']} - leave blank to keep old value")
            # taking new values, keeping old if user leaves blank
            new_name = input(f"New Name ({s['name']}): ").strip()
            new_age = input(f"New Age ({s['age']}): ").strip()
            new_course = input(f"New Course ({s['course']}): ").strip()

            if new_name != "":
                s["name"] = new_name
            if new_age != "":
                if not new_age.isdigit():
                    print("Age must be a number! Skipping age update.")
                else:
                    s["age"] = int(new_age)
            if new_course != "":
                s["course"] = new_course

            save_students(students)
            print("Student updated successfully!")
            return
    print("No student found with this ID!")

# deleting student by id
def delete_student():
    students = load_students()
    print("\nDelete Student-  ")
    sid = input("Enter Student ID to delete: ").strip()
    new_list = []
    deleted = False
    for s in students:
        if s["id"] == sid:
            deleted = True  # skip this student (delete it)
            print(f"Student {s['name']} deleted!")
        else:
            new_list.append(s)  # keep everyone else
    if not deleted:
        print("No student found with this ID!")
    else:
        save_students(new_list)

# main menu
def main():
    print("Student Record Manager!")
    print("Made by Garima\n")

    while True:
        # showing menu options
        print("\nMAIN MENU      ")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        choice = input("\nEnter your choice (1-6): ").strip()
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 6.")
# starting the program
main()