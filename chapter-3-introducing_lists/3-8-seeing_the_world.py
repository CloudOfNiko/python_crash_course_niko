# CloudOfNiko
# 29.01.2026

# Create a list and print it.
places = ["hammerfell", "elsweyr", "cyrodiil", "skyrim", "morrowind"]
print(places)

# Temporarily sort the list alphabetically without storing the new order and print both the sorted and unchanged list.
print(f"\n{sorted(places)}")
print(f"\n{places}")

# Temporarily sort the list reverse-alphabetically without storing the new order and print both the sorted and unchanged list.
print(f"\n{sorted(places, reverse=True)}")
print(f"\n{places}")

# Reverse the list order permanently and print it.
places.reverse()
print(f"\n{places}")

# Reverse the changed list to return to the original order and print it.
places.reverse()
print(f"\n{places}")

# Permanently sort the list alphabetically and print it.
places.sort()
print(f"\n{places}")

# Permanently sort the list reverse-alphabetically and print it.
places.sort(reverse=True)
print(f"\n{places}")