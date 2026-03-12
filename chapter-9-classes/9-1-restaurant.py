# CloudOfNiko
# 12.03.2026
# Learning to use classes in Python.
# Includes 9-1 and 9-3.

class Restaurant:
    """Make a basic model of a restaurant."""

    def __init__(self, name, cuisine):
        """Initialize restaurant name and cuisine type attributes."""
        self.name = name
        self.cuisine = cuisine
    
    def describe_restaurant(self):
        """Print the restaurant name and its cuisine type."""
        print(self.name)
        print(self.cuisine)

    def open_restaurant(self):
        """Print a message indicating the restaurant is open."""
        print(f"{self.name} is now open!")

restaurant = Restaurant("Tun Lahmajo", "Armenian")
restaurant_1 = Restaurant("Khinkali Bar №1", "Georgian")
restaurant_2 = Restaurant("Kawaii Sushi", "Japanese")

restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()

restaurant_2.describe_restaurant()
restaurant_2.open_restaurant()