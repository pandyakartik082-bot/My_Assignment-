# 5.
# Create a program that uses a while loop to print a pyramid star pattern with 4 rows, so the output looks like BookMyShow's seat rows:
# *
# ***
# *****
# *******<br><br><em><strong>Hint:</strong> Use two nested while loops: one for spaces, one for stars.</em>

i = 1

while i <= 4:
    space = 1

    while space <= 4 - i:
        print(" ", end="")
        space += 1

    star = 1

    while star <= 2 * i - 1:
        print("*", end="")
        star += 1

    print()
    i += 1