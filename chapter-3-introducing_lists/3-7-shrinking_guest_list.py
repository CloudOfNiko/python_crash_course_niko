# CloudOfNiko
# 28.01.2026
# This is a variation of 3-6, where we leave only two people in the list, leaving an apologetic message to each, and then empty out the list completely.

guests = ['frieren', 'fern', 'stark']

print(f"Welcome, {guests[0].title()}! Shall we go?")
print(f"Greetings, {guests[1].title()}! Would you like some sweets?")
print(f"Hello, {guests[2].title()}! How about we test your mettle?")

print("\n")

print("We've found a bigger table for the feast!")

print("\n")

guests.insert(0, 'himmel')
guests.insert(2, 'heiter')
guests.append('eisen')

print(f"Good morning, {guests[0].title()}! Only the finest ingredients for you.")
print(f"Welcome, {guests[1].title()}! Shall we go?")
print(f"Hello there, {guests[2].title()}! We better hide the drinks...")
print(f"Greetings, {guests[3].title()}! Would you like some sweets?")
print(f"Hello, {guests[4].title()}! How about we test your mettle?")
print(f"Welcome back, {guests[5].title()}! Quiet as usual, eh?")

print("\n")

print("Oh no! The table for six won't arrive in time!")

print("\n")

print(f"Our apologies for the inconvenience, {guests.pop().title()}. You're invited to the next gathering.")
print(f"Our apologies for the inconvenience, {guests.pop().title()}. You're invited to the next gathering.")
print(f"Our apologies for the inconvenience, {guests.pop().title()}. You're invited to the next gathering.")
print(f"Our apologies for the inconvenience, {guests.pop().title()}. You're invited to the next gathering.")

print('\n')

print(f"Good morning, {guests[0].title()}! Only the finest ingredients for you.")
print(f"Welcome, {guests[1].title()}! Shall we go?")

print('\n')

del guests[1]
del guests[0]
print(guests)