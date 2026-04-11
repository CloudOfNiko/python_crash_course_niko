# CloudOfNiko
# 11.04.2026
# Learning how to read files in Python.

from pathlib import Path

path = Path('chapter-10-files_and_exceptions/guest.txt')
name = input('Enter your name: ')
path.write_text(name)
print(path.read_text())