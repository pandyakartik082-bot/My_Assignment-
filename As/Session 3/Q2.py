# 2.
# Create a small program that takes two numbers as input (use input()), converts them to integers using int(), and prints their sum, difference, product, and quotient using print().<br><br><em><strong>Hint:</strong> Remember to convert the input strings to integers before performing arithmetic operations.</em>


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)

if num2 != 0:
    print("Quotient:", num1 / num2)
else:
    print("Cannot divide by zero")