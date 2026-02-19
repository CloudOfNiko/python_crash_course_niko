# CloudOfNiko
# 20.02.2026
# Learning to use dictionaries in Python.
# Went with some of the 13 squads' members instead of numbers as I did
# 6-2 differently.

squads = {
    '1' : ['Genryūsai Shigekuni Yamamoto', 'Chōjirō Sasakibe'],
    '2' : ['Soi Fon', 'Marechiyo Ōmaeda'],
    '3' : ['Rōjūrō "Rose" Ōtoribashi', 'Izuru Kira']
    }

for squad in squads:
    print(f"\nDivision №{squad}'s Captain and Lieutenant are:")
    names = squads[squad]
    for name in names:
        print(f"\t{name}")