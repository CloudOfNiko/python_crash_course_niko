# CloudOfNiko
# 22.02.2026
# Learning to get user input through Python.

people_number = input("How many people are you reserving a table for? ")
people_number = int(people_number)

if people_number < 1:
    print(f"Please enter a valid number.")
elif people_number <= 8:
    print(f"Your table for {people_number} is ready!")
else:
    print(f"Unfortunately, a table for {people_number} is unavailable.")