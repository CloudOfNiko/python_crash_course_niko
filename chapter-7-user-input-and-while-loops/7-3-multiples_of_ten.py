# CloudOfNiko
# 22.02.2026
# Learning to get user input through Python.

prompt = "This program can check whether a number is a multiple of 10."
prompt += "\nPlease input a number: "

number = input(prompt)
number = int(number)

if number % 10 == 0:
    print(f"\n{number} is a multiple of ten.")
else:
    print(f"\n{number} is not a multiple of ten.")
