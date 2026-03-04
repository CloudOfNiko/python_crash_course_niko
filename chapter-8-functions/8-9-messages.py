# CloudOfNiko
# 04.03.2026
# Learning to use functions in Python.
# Includes 8-9, 8-10 and 8-11.

msgs = ['Hello!', 'Goodbye!', 'Later!']
sent_msgs = []

def show_messages(messages):
    """Display all messages from a list."""
    for message in messages:
        print(message)

show_messages(msgs)
print(f"\n")

def send_messages(unsent_messages, sent_messages):
    """Simulate sending messages by printing the messages from a list and moving them to another list."""
    while unsent_messages:
        current_message = unsent_messages.pop()
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)

send_messages(msgs, sent_msgs)

print(msgs)
print(sent_msgs)
print(f"\n")

archived_msgs = []

send_messages(sent_msgs[:], archived_msgs)

print(sent_msgs)
print(archived_msgs)