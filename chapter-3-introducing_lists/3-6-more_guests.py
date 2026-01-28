# CloudOfNiko
# 28.01.2026
# This is another alternative version of 3-4, where we add a new group of guests to the list by practicing new methods.

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