# CloudOfNiko
# 11.02.2026
# Learning how to use slices with Python lists.

pizzas = ['hawaiian', 'quatro formaggio', 'mexican']

for pizza in pizzas:
    print(pizza)

print(f"\n")

for pizza in pizzas:
    print(f"I like {pizza.title()} pizza!")

print(f"\nPizza is very cool.")

friend_pizzas = pizzas[:]

pizzas.append("margherita")
friend_pizzas.append("neapolitan")

print(f"\nMy favourite pizzas are:")
for pizza in pizzas:
    print(pizza.title())

print(f"\nMy friend's favourite pizzas are:")
for pizza in friend_pizzas:
    print(pizza.title())