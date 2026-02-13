# CloudOfNiko
# 14.02.2026
# Learning to use if statements with lists in Python.

ordinal_numbers = [number for number in range(1,10)]

for number in ordinal_numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    elif number > 3:
        print(f"{number}th")