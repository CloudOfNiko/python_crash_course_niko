# CloudOfNiko
# 11.02.2026
# Learning how to use slices with Python lists.

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

# Used code from the book.

for food in my_foods:
    print(food.title())

print("\n")

for food in friend_foods:
    print(food.title())