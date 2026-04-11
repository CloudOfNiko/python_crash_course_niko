# CloudOfNiko
# 11.04.2026
# Learning how to read files in Python.

from pathlib import Path

path = Path('chapter-10-files_and_exceptions/guest_book.txt')

name = ''
names = ''

while True:
    print('Enter "exit" to quit.')
    name = input('Enter your name: ')
    if name == 'exit':
        break
    else:
        names += f"{name}\n"
    
path.write_text(names)
print(path.read_text())