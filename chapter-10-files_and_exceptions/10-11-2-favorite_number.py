# CloudOfNiko
# 18.04.2026
# Learning how to use the json module.

from pathlib import Path
import json

path = Path('favorite_number.json')
favorite_number = path.read_text()

print(f"Your favorite number is {favorite_number}!")