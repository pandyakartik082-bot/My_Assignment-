# 3.
# Build a function reverse_message(message) that reverses any string passed to it, similar to how WhatsApp displays reversed text stickers.<br><br><em><strong>Constraint:</strong> Do not use Python's built-in reversed() or [::-1] slicing shortcut.</em>




def reverse_message(message):
    reverse = ""

    for char in message:
        reverse = char + reverse

    return reverse

message = input("Enter your message: ")

print("Reversed Message:", reverse_message(message))