# CloudOfNiko
# 26.02.2026
# Learning about 'while' loops in Python.

# Create empty dictionary for user replies.
responses = {}

# Make flag to indicate that polling is active.
polling_active = True

while polling_active:
    # Prompt user for the name and response.
    name = input("\nWhat is your name? ")
    response = input("Where are you dreaming of going for a vacation? ")

    # Store reply.
    responses[name] = response

    # Check if anyone else wants to do the poll.

    repeat = input("Would you like to let another person answer the poll? (yes/no) ")
    if repeat == 'no':
        polling_active = False

#Show results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to travel to {response}.")