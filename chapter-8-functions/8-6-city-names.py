# CloudOfNiko
# 03.03.2026
# Learning to use functions in Python.

def get_city_country(city, country):
    """Return the user input as a formatted string for city and its country."""
    string = f"{city}, {country}"
    return string.title()

city_country = get_city_country('rostov', 'russia')
print(city_country)
city_country = get_city_country('yerevan', 'armenia')
print(city_country)
city_country = get_city_country('tbilisi', 'georgia')
print(city_country)