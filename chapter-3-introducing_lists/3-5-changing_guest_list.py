# CloudOfNiko
# 28.01.2026
# This is an extended version of 3-4, where one of the guests is removed from the list, and a new guest is added instead, and a new set of greetings is displayed.

guests = ['frieren', 'fern', 'stark']

print(f"Welcome, {guests[0].title()}! Shall we go?")
print(f"Greetings, {guests[1].title()}! Would you like some sweets?")
print(f"Hello, {guests[2].title()}! How about we test your mettle?")

print("\n")

print(f"{guests.pop(1)}")

print("\n")

guests.append("sein")

print(f"Welcome, {guests[0].title()}! Shall we go?")
print(f"Hello, {guests[1].title()}! How about we test your mettle?")
print(f"Hey there, {guests[2].title()}! Care for a drink?")