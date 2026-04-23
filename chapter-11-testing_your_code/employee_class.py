# CloudOfNiko
# 23.04.2026
# Learning to use fixtures in pytest.

class Employee:
    """Basic representation of an employee at a company."""
    
    def __init__(self, first_name, last_name, salary):
        """Initialize employee's basic attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, amount=5000):
        """Increase employee's salary by 5000 or a user-defined amount."""
        self.salary += amount