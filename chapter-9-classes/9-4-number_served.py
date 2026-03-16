# CloudOfNiko
# 15.03.2026
# Learning to use classes in Python.

class Restaurant:
    """Make a basic model of a restaurant."""

    def __init__(self, name, cuisine):
        """Initialize restaurant name and cuisine type attributes."""
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0
    
    def describe_restaurant(self):
        """Print the restaurant name and its cuisine type."""
        print(self.name)
        print(self.cuisine)

    def open_restaurant(self):
        """Print a message indicating the restaurant is open."""
        print(f"{self.name} is now open!")

    def set_number_served(self, customers):
        """Set the number of customers that have been served."""
        self.number_served = customers

    def increment_number_served(self, increment_customers):
        """Add the given number of customers that have been served."""
        self.number_served += increment_customers

    def display_number_served(self):
        """Print the amount of served customers."""
        print(f"This restaurant has served {self.number_served} customers.")

restaurant = Restaurant("Tun Lahmajo", "Armenian")

restaurant.set_number_served(40)
restaurant.display_number_served()

restaurant.increment_number_served(15)
restaurant.display_number_served()