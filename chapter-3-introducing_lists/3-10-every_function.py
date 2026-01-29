# CloudOfNiko
# 29.01.2026
# This code displays the different functions from Chapter 3 interacting with a list.

phantom_thieves = ["joker", "mona", "skull", "panther", "fox", "queen", "noir"] # hope I didn't forget anyone lmao
print(phantom_thieves)

print(f"{phantom_thieves[0].title()}")

phantom_thieves.append("crow")
print(phantom_thieves)

phantom_thieves.insert(1, 'wonder')
print(phantom_thieves)

del phantom_thieves[1]
print(phantom_thieves)

print(phantom_thieves.pop())
print(phantom_thieves)

phantom_thieves.remove('mona')
print(phantom_thieves)

phantom_thieves.sort()
print(phantom_thieves)

print(sorted(phantom_thieves, reverse=True))

phantom_thieves.reverse()
print(phantom_thieves)

print(len(phantom_thieves))