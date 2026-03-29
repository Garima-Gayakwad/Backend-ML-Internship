# arguments - calling function using keyword arguments
def student_info(name, age, course):
    print(f"Student Name: {name}")
    print(f"Age: {age}")
    print(f"Course: {course}")
    print("  ")
# calling with keyword arguments
student_info(name="Garima", age=20, course="Computer Science")
student_info(name="Rohan", age=21, course="IT")
student_info(name="Neha", age=19, course="Data Science")