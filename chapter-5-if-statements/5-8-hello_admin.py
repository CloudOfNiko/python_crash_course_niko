# CloudOfNiko
# 14.02.2026
# Learning to use if statements with lists in Python.
# Includes 5-8 and 5-9.

usernames = ['admin', 'Solocamper8', 'StaleGrapes', 'Tacocat60', 'WigglyCow']

if usernames:
    for username in usernames:
        if username == 'admin':
            print(f"The Zero Point awaits, {username}.")
        else:
            print(f"Remember to thank the bus driver, {username}.")
else:
    print("The bus is empty!")