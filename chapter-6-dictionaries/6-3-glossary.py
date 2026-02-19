# CloudOfNiko
# 15.02.2026
# Learning to use dictionaries in Python.
# Looked up how to get the key names without knowing them for use in a loop.
# Includes 6-3 and 6-4.

glossary = {
    'variable' : 'A symbolic name that references an object stored in memory.',
    'list' : 'An ordered and mutable collection data type used to store multiple items in a single variable.',
    'tuple' : 'An ordered and immutable collection of items',
    'dictionary' : 'A data type that stores data as a collection of key-value pairs.',
    'method' : 'A function that is defined inside a class and operates on an object (instance) of that class.',
    'set' : 'An unordered collection of unique elements.',
    'key' : 'A unique identifier used to store and access values in a dictionary.',
    'loop' : 'A control flow statement that allows a block of code to be executed repeatedly until a specific condition is met or for each item in a sequence.',
    'statement' : 'A complete instruction that the interpreter can execute to perform an action or control program flow.',
    'boolean' : 'A fundamental data type that can have only one of two values: true or false'
    }

for word, meaning in glossary.items():
    print(f"\n{word.title()} - {meaning}")