# CloudOfNiko
# 15.02.2026
# Learning to use dictionaries in Python.

glossary = {
    'variable' : 'A symbolic name that references an object stored in memory.',
    'list' : 'An ordered and mutable collection data type used to store multiple items in a single variable.',
    'tuple' : 'An ordered and immutable collection of items',
    'dictionary' : 'A data type that stores data as a collection of key-value pairs.',
    'method' : 'A function that is defined inside a class and operates on an object (instance) of that class.'
}

for word, meaning in glossary.items():
    print(f"\n{word.title()} - {meaning}")