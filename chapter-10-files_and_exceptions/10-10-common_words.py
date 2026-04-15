# CloudOfNiko
# 15.04.2026
# Learning how to handle exceptions in Python.

from pathlib import Path

book = Path('chapter-10-files_and_exceptions/moby.txt').read_text()
the = book.lower().count('the ')

print(f"The book uses the word 'the' {the} times.")