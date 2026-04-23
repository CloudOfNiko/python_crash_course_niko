# CloudOfNiko
# 23.04.2026
# Learning to use pytest.


from city_functions import get_formatted_city

def test_city_country():
    """Do cities like 'Yerevan, Armenia' work?"""
    city_country = get_formatted_city('yerevan', 'armenia')
    assert city_country == 'Yerevan, Armenia'

def test_city_country_population():
    """Do cities like 'Tbilisi, Georgia - population 3,704,500' work?"""
    city_country = get_formatted_city('tbilisi', 'georgia', '3,704,500')
    assert city_country == 'Tbilisi, Georgia - population 3,704,500'