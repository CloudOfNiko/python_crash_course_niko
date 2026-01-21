# CloudOfNiko
# 20.01.2026
# This code assigns a correctly titled and whitespace-stripped string to the two variables, and then correctly formats
# the full name in a message.
first_name = "vazgen"
first_name = first_name.title().strip()
last_name = "tumanyan"
last_name = last_name.title().strip()
full_name = f"{first_name} {last_name}"
message = f"{full_name}, how are you today?"
print(message)