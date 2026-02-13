# CloudOfNiko
# 13.02.2026
# Learning how to use conditional tests in Python.
# Includes 5-1 and 5-2.

pony = 'Applejack'
print("Is pony == 'Applejack'? I predict True.")
print(pony == 'Applejack')

print("\nIs pony.lower() == 'applejack'? I predict True.")
print(pony.lower() == 'applejack')

print("\nIs pony.upper() == 'APPLEJACK'? I predict True.")
print(pony.upper() == 'APPLEJACK')

print("\nIs pony.lower() == 'applejack'? I predict True.")
print(pony.lower() == 'applejack')

print("\nIs pony == 'Applejack' or pony == 'Rarity'? I predict True.")
print(pony == 'applejack' or pony == 'Rarity')

print("\nIs pony == 'Rarity'? I predict False.")
print(pony == 'Rarity')

print("\nIs pony == 'Fluttershy'? I predict False.")
print(pony == 'Fluttershy')

print("\nIs pony == 'Fluttershy' and pony == 'Applejack'? I predict False.")
print(pony == 'Fluttershy' and pony == 'Applejack')

balloons = 10
print("\nIs balloons == 10? I predict True.")
print(balloons == 10)

print("\nIs balloons >= 10? I predict True.")
print(balloons >= 10)

print("\nIs balloons <= 10? I predict True.")
print(balloons <= 10)

print("\nIs balloons < 10? I predict False.")
print(balloons < 10)

print("\nIs balloons > 10? I predict False.")
print(balloons > 10)

print("\nIs balloons != 10? I predict False.")
print(balloons != 10)

cutie_mark_crusaders = ['Applebloom', 'Scootaloo', 'Sweetie Belle']
print("\nIs 'Applebloom' in cutie_mark_crusaders? I predict True.")
print('Applebloom' in cutie_mark_crusaders)

print("\nIs 'Babs Seed' in cutie_mark_crusaders? I predict False.")
print('Babs Seed' in cutie_mark_crusaders)