# CloudOfNiko
# 15.04.2026
# Learning how to handle exceptions in Python.
# Includes 10-8 and 10-9.

from pathlib import Path

try:
    cats = Path('chapter-10-files_and_exceptions/cats.txt').read_text()
    dogs = Path('chapter-10-files_and_exceptions/dogs.txt').read_text()
    print(cats)
    print(dogs)
except FileNotFoundError:
    pass