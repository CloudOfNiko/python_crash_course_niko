# CloudOfNiko
# 18.04.2026
# Learning how to use the json module.

from pathlib import Path
import json

favorite_number = input("Enter your favorite number: ")

path = Path('favorite_number.json')
contents = json.dumps(favorite_number)
path.write_text(contents)

print(f"Number {favorite_number} stored.")