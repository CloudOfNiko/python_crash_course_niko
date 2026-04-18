# CloudOfNiko
# 18.04.2026
# Learning how to use the json module.

from pathlib import Path
import json

path = Path('favorite_number.json')

if path.exists():
    favorite_number = path.read_text()
    print(f"Your favorite number is {favorite_number}!")
else:
    favorite_number = input("Enter your favorite number: ")
    contents = json.dumps(favorite_number)
    path.write_text(contents)
    print(f"Number {favorite_number} stored.")