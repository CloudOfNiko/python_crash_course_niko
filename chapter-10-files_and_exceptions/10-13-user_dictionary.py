# CloudOfNiko
# 21.04.2026
# Learning how to use the json module.

from pathlib import Path
import json

def get_stored_info(path):
    """Get stored user information if available."""
    if path.exists():
        contents = path.read_text()
        user = json.loads(contents)
        return user
    else:
        return None

def get_new_info(path):
    """Prompt for new user information."""
    user = {}
    username = input("What is your name? ")
    user['username'] = username
    age = input("How old are you? ")
    user['age'] = age
    country = input("What is your country of residence? ")
    user['country'] = country    
    contents = json.dumps(user)
    path.write_text(contents)
    return user

def greet_user():
    """Greet the user with previously prompted info."""
    path = Path('user.json')
    user = get_stored_info(path)
    if user:
        print(f"Welcome back, {user['username']}!")
        print(f"You are {user['age']} years old.")
        print(f"How's the weather in {user['country']}?")
    else:
        user = get_new_info(path)
        print(f"We'll remember you when you come back, {user['username']}!")

greet_user()