# 4.
# Build a Python script that asks the user to enter a word (like a song name), then uses a for loop to print each character on a new line, but only if the character is a vowel (a, e, i, o, u).<br><br><em><strong>Constraint:</strong> Do not use the 'in' operator inside your if statement — use multiple '==' checks instead.</em>

word = input("Enter a word: ")

for char in word:
    if char.lower() == 'a' or char.lower() == 'e' or char.lower() == 'i' or char.lower() == 'o' or char.lower() == 'u':
        print(char)