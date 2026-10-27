# 4.
# Given a dictionary called food_order = {'Pizza': 2, 'Burger': 1, 'Fries': 3}, use the keys(), values(), and items() methods to print: a) all food items, b) all quantities, and c) each item with its quantity.


food_order = {'Pizza': 2, 'Burger': 1, 'Fries': 3}

# a) Print all food items
print("Food Items:", food_order.keys())

# b) Print all quantities
print("Quantities:", food_order.values())

# c) Print each item with its quantity
print("Items with Quantities:")

for item, qty in food_order.items():
    print(item, ":", qty)