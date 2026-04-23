# CloudOfNiko
# 23.04.2026
# Learning to use pytest.
# Includes 11-1 and 11-2.

def get_formatted_city(city, country, population=''):
    """Return a neatly formatted 'City, Country - population xxx' string."""
    if population:
        city_country = f"{city.title()}, {country.title()} - population {population}"
    else:
        city_country = f"{city.title()}, {country.title()}"
    return city_country