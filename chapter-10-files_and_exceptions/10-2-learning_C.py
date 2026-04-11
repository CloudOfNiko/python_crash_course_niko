# CloudOfNiko
# 11.04.2026
# Learning how to read files in Python.

from pathlib import Path
path = Path('chapter-10-files_and_exceptions/learning_python.txt')
contents = path.read_text()

new_line = ''

for line in contents.splitlines():
    new_line = line.replace('Python', 'C')
    print(new_line)