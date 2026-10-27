# 5.
# Using reduce() and a lambda function, calculate the total bill amount for a Swiggy order given a list of item prices: [120, 80, 150, 60].<br><br><em><strong>Hint:</strong> Import reduce from functools.</em>


from functools import reduce

# List of item prices
prices = [120, 80, 150, 60]

# Calculate total bill using reduce() and lambda
total_bill = reduce(lambda a, b: a + b, prices)

print("Swiggy Order Prices:", prices)
print("Total Bill Amount: ₹", total_bill)