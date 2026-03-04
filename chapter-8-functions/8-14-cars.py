# CloudOfNiko
# 05.03.2026
# Learning to use functions in Python.

def make_car(manufacturer_name, model_name, **car_info):
    """Store information about a car."""
    car_info['manufacturer'] = manufacturer_name
    car_info['model'] = model_name
    return car_info

car_profile = make_car('Honda', 'Civic', year='2006', engine='1.8L', transmission='manual')
print(car_profile)