# CloudOfNiko
# 23.03.2026

"""A set of classes that can be used to represent elevated User privileges."""

from user import User

class Privileges:
    """Create a class storing privileges."""
    def __init__(self):
        """Initialize privileges."""
        self.privileges = ["can add post", "can delete post", "can add user"]
    
    def show_privileges(self):
        """List user privileges."""
        print("Privileges:")
        for privilege in self.privileges:
            print(privilege)

class Admin(User):
    """Create a special kind of user, with admin privileges."""
    def __init__(self, first_name, last_name, age=None, occupation=None, sex=None):
        """Initialize admin's attributes."""
        super().__init__(first_name, last_name, age, occupation, sex)
        self.privileges = Privileges()