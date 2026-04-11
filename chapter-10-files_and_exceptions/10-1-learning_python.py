# CloudOfNiko
# 11.04.2026
# Learning how to read files in Python.

from pathlib import Path

path = Path('chapter-10-files_and_exceptions/learning_python.txt')
contents = path.read_text()

print(contents)

lines_split = []
for line in contents.splitlines():
    lines_split.append(line)

for line in lines_split:
    print(line)