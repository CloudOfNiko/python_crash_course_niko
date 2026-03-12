# CloudOfNiko
# 12.03.2026
# Learning to use classes in Python.

class User:
    """Make a basic user."""
    def __init__(self, first_name, last_name, age=None, occupation=None, sex=None):
        """Store user's first and last name as required, then age, occupation and sex optionally."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.occupation = occupation
        self.sex = sex

    def describe_user(self):
        """Create a basic user description."""
        print(f"User Information:")
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")

        if self.age == None:
            print("Age not provided.")
        else:
            print(f"Age: {self.age}")
        
        if self.occupation == None:
            print("Occupation not provided.")
        else:
            print(f"Occupation: {self.occupation}")

        if self.sex == None:
            print("Sex not provided.")
        else:
            print(f"Sex: {self.sex}")

    def greet_user(self):
        """Generate a basic user greeting."""
        print(f"Welcome back, {self.first_name}.")

user_1 = User("Celty", "Sturluson", occupation="Transporter", sex="Female")
user_1.describe_user()
print(f"\n")
user_1.greet_user()
print(f"\n")
user_2 = User("Izaya", "Orihara", 23, "Information Broker", "Male")
user_2.describe_user()
print(f"\n")
user_2.greet_user()
print(f"\n")
user_3 = User("Mikado", "Ryuugamine", 16, "Student", "Male")
user_3.describe_user()
print(f"\n")
user_3.greet_user()