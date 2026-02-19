# CloudOfNiko
# 20.02.2026
# Learning to use dictionaries in Python.

cities = {
    'Limsa Lominsa' : {
        'location' : 'Vylbrand',
        'affiliation' : 'The Maelstrom',
        'patron_deity' : 'Llymlaen'
        },
    'Gridania' : {
        'location' : 'The Black Shroud',
        'affiliation' : 'Order of the Twin Adder',
        'patron_deity' : 'Nophica'
        },
    "Ul'dah" : {
        'location' : 'Southern Aldenard',
        'affiliation' : 'Immortal Flames',
        'patron_deity' : "Nald'thal"
        }
    }

for name, info in cities.items():
    print(f"\n{name}:")
    for key, value in info.items():
        print(f"\t{key.title()}: {value}")