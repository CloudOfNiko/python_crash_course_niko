# CloudOfNiko
# 15.02.2026
# Learning to use dictionaries in Python.
# Includes 6-1 and 6-7.

unit_0 = {
    'name' : 'YoRHa No.2 Type B',
    'occupation' : 'YoRHa Soldier Unit',
    'race' : 'Android',
    'sex' : 'Female',
    'born' : 'January 7, 11942'
           }

unit_1 = {
    'name' : 'YoRHa No.9 Type S',
    'occupation' : 'YoRHa Scanner Unit',
    'race' : 'Android',
    'sex' : 'Male',
    'born' : 'January 30, 11942'
           }

unit_2 = {
    'name' : 'YoRHa Type A No.2',
    'occupation' : 'YoRHa Attacker Unit',
    'race' : 'Android',
    'sex' : 'Female',
    'born' : 'May 20, 11941'
           }

units = [unit_0, unit_1, unit_2]

for unit in units:
    print(f"\n{unit['name']}")
    print(f"\n\tType: {unit['occupation']}")
    print(f"\tRace: {unit['race']}")
    print(f"\tSex: {unit['sex']}")
    print(f"\tCreated on: {unit['born']}")