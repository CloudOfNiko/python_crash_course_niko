# CloudOfNiko
# 23.02.2026
# Learning about 'while' loops in Python.
# Includes 7-5 and 7-6, I guess.

#Starting with the prompt.
prompt = "Please enter your age."
prompt += "\n(To exit enter 'quit'.) "

message = ""

#Setting a flag to keep the program running.
active = True

while active:
    message = input(f"\n{prompt}")

#Quitting loop if 'quit' is entered to avoid int error.
    if message == 'quit':
        break

    else:
        message = int(message)

#Restarting loop if age is under 0.
        if message < 0:
            print("\nPlease enter a valid age.")
            continue
        elif message < 3:
            print("\nYour ticket is free.")
            break
        elif message <= 12:
            print("\nYour ticket is $10.")
            break
        elif message > 12:
            print("\nYour ticket is $15.")
            break