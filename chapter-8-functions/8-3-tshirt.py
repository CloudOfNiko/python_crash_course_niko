# CloudOfNiko
# 27.02.2026
# Learning about functions in Python.
# Includes 8-3 and 8-4.

def make_shirt(size='L', text='I love Python!'):
    """Collect information for the user's desired T-Shirt size and text on it."""
    print(f"\nYou're ordering a size {size.title()} T-Shirt.")
    print(f'"{text}" will be written on it.')

make_shirt('M', "Your mom's a hamster!")

make_shirt(size='S', text='Wake me up!')

make_shirt()