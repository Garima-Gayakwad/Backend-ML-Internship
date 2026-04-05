# user classes using inheritance and polymorphism
# ABSTRACTION - base User class
class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed = []  # list of borrowed book ids
    # child classes override this
    def get_role(self):
        return "User"
    def __str__(self):
        return f"{self.get_role()}: {self.name} (ID: {self.user_id})"

# INHERITANCE - student inherits from User
class Student(User):
    def __init__(self, name, user_id):
        super().__init__(name, user_id)
        self.borrow_limit = 3  # students can only borrow 3 books max

    # POLYMORPHISM - overrides get_role
    def get_role(self):
        return "Student"

# INHERITANCE - librarian also inherits from User
class Librarian(User):
    def __init__(self, name, user_id):
        super().__init__(name, user_id)
        self.borrow_limit = 10  # librarians can borrow more

    # POLYMORPHISM - different role than student
    def get_role(self):
        return "Librarian"