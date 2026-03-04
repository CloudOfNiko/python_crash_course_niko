# CloudOfNiko
# 05.03.2026
# Learning to use functions in Python.

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('Ren', 'Amamiya', occupation='student', age='17', persona='Arsène')
print(user_profile)