# CloudOfNiko
# 20.02.2026
# Learning to use dictionaries in Python.

favorite_places = {
    '2B' : ['City Ruins', 'Copied City'],
    '9S' : ['Desert Zone', 'Tower'],
    'A2' : ['Resistance Camp', "Pascal's Village"],  
    }

for name in favorite_places:
    print(f"\nThese are {name}'s favorite places:")
    places = favorite_places[name]
    for place in places:
        print(place)