# CloudOfNiko
# 15.04.2026
# Learning how to handle exceptions in Python.

print("Enter two numbers to add them together.")

first_number = input("\nFirst number: ")
second_number = input("Second number: ")
try:
    answer = int(first_number) + int(second_number)
except ValueError:
    print("\nPlease enter numbers.")
else:
    print(f"\n{answer}")