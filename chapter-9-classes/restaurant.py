# CloudOfNiko
# 23.03.2026

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