# CloudOfNiko
# 14.02.2026
# Learning to use if statements with lists in Python.

current_users = ['admin', 'Solocamper8', 'StaleGrapes', 'Tacocat60', 'WigglyCow']

lower_users = []

new_users = ['SOlocamper8', 'TroubledTaco45', 'WalkTheDog80', 'WigglyCow', 'WrathofKnight']

for user in current_users:
    lower_users.append(user.lower())
    
for user in new_users:
    if user.lower() in lower_users:
        print(f"The {user} username is not available.")
    else:
        print(f"Welcome, {user}.")