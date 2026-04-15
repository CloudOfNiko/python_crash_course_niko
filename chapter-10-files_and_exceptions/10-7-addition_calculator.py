# CloudOfNiko
# 15.04.2026
# Learning how to handle exceptions in Python.

print("Enter two numbers to add them together.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("\nPlease enter numbers.")
    else:
        print(f"\n{answer}")