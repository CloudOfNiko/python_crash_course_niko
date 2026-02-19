# CloudOfNiko
# 20.02.2026
# Learning to use dictionaries in Python.

favorite_languages = {
      'jen': ['python', 'rust'],
      'sarah': ['c'],
      'edward': ['rust', 'go'],
      'phil': ['python', 'haskell'],
      }

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")

print("\n")

names = ['john', 'jen', 'kratos', 'joe', 'scrooge', 'edward']

for name in names:
    if name in favorite_languages:
        print(f"Thank you for taking our poll, {name.title()}!")
    if name not in favorite_languages:
        print(f"Please take our poll, {name.title()}.")