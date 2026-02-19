# CloudOfNiko
# 19.02.2026
# Learning to use dictionaries in Python.

rivers = {
    'Kura' : 'Georgia',
    'Araks' : 'Armenia',
    'Neva' : 'Russia'
    }

# Print a sentence for each key, value pair in the dicionary.
for river, country in rivers.items():
    print(f"The {river.title()} river runs through {country.title()}.")

print("\n")

# Print a titled key name for each key stored in the dictionary. 
for river in rivers.keys():
    print(river.title())

print("\n")

# Print a titled value name for each value stored in the dictionary. 
for country in rivers.values():
    print(country.title())