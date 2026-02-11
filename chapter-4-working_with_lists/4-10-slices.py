# CloudOfNiko
# 11.02.2026
# Learning to use slices with Python lists.

numbers = [odder for odder in range(1,21,2)]

for odder in numbers:
    print(odder)

print(f"The first three items in the list are: {numbers[:3]}")
print(f"Three items in the middle of the list are: {numbers[2:5]}")
print(f"The last three items in the list are: {numbers[-3:]}")