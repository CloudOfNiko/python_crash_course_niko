# CloudOfNiko
# 23.03.2026
# Learning to use default Python modules.
# Includes 9-14 and 9-15.

from random import choice

options = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, "a", "b", "c", "d", "e"]

def get_winners(entries):
    """Generate 4 winners in a lottery."""
    winning_ticket = []
    while len(winning_ticket) < 4:
        winner = choice(entries)
        if winner not in winning_ticket:
            winning_ticket.append(winner)
    return winning_ticket

def check_ticket(ticket, winner):
    """Check if current ticket has won."""
    for element in ticket:
        if element not in winner:
            return False
    return True

current_winner = get_winners(options)

print(f"The winning symbols are:\n{current_winner}")

print("\n")

won = False
attempts = 0

while not won:
    attempts += 1
    my_ticket = get_winners(options)
    won = check_ticket(my_ticket, current_winner)

print(f"It took {attempts} tries to win.\nYou will never financially recover.")