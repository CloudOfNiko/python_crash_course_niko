# CloudOfNiko
# 23.02.2026
# Learning about 'while' loops in Python.
# Includes 7-4 and 7-6, I guess.

prompt = "\nEnter your desired pizza toppings."
prompt += "\n(Enter 'quit' when you're finished.) "

message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(f"\n{message}")