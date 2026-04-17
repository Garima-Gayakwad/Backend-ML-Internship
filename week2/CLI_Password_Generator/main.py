from faker import Faker
from password_utils import generate_password
# faker helps generate fake data like usernames
fake = Faker()
print("Garima's Password Generator\n")
# generating a random username suggestion using faker
username = fake.user_name()
print(f"Suggested username: {username}")
# asking user for password length with exception handling
try:
    length = int(input("\nEnter password length (e.g. 12): "))
    if length <= 0:
        print("length must be greater than 0!")
    elif length < 6:
        print("too short! use at least 6 characters for security")
    else:
        pwd = generate_password(length)
        print(f"\nGenerated Password : {pwd}")
        print(f"Password Length    : {length}")
except ValueError:
    print("invalid input! please enter a number, not text")