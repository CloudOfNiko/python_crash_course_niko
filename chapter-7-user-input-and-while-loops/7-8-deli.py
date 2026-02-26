# CloudOfNiko
# 26.02.2026
# Learning about 'while' loops in Python.
# Included 7-8 and 7-9.

#Make a list for different sandwich names.
sandwich_orders = ['pastrami', 'BLT', 'panini', 'club', 'pastrami', 'grilled cheese', 'turkey & cheddar', 'pastrami']

#Make an empty list for completed orders.
finished_sandwiches = []

#Remove pastrami from the list.
print("Sorry, pastrami sandwiches are not currently available.\n")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')


#Process each sandwich name and move it to the finished list.
#Keep BLT capitalized so it looks nice in the output.
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    
    if current_sandwich == 'BLT':
        print(f"Preparing {current_sandwich.upper()}...")
        finished_sandwiches.append(current_sandwich)
    else:
        print(f"Preparing {current_sandwich.title()}...")
        finished_sandwiches.append(current_sandwich)

#Show finished orders.
print("\nFollowing orders have been completed:")
for finished_sandwich in finished_sandwiches:
    if finished_sandwich == 'BLT':
        print(finished_sandwich.upper())
    else:
        print(finished_sandwich.title())