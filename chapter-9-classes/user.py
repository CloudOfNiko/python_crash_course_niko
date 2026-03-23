# CloudOfNiko
# 23.03.2026

"""A class used to represent a User."""

class User:
    """Make a basic user."""
    def __init__(self, first_name, last_name, age=None, occupation=None, sex=None):
        """Store user's first and last name as required, then age, occupation and sex optionally."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.occupation = occupation
        self.sex = sex
        self.login_attempts = 0

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

    def increment_login_attempts(self):
        """Add the given number of customers that have been served."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the amount of login attempts to 0."""
        self.login_attempts = 0

    def display_login_attempts(self):
        """Print the amount of login attempts for this user."""
        print(f"Login attempts: {self.login_attempts}")