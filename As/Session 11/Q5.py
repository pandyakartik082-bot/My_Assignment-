# 5.
# Build a function update_cart(cart, item, qty) that adds a new item to a Flipkart-style cart dictionary or updates the quantity if the item already exists, then returns the updated cart.<br><br><em><strong>Hint:</strong> Use the dictionary's update() method or direct assignment for adding/updating entries.</em>


def update_cart(cart, item, qty):
    cart.update({item: qty})
    return cart

cart = {"Mobile": 1, "Laptop": 2}

print("Original Cart:", cart)

update_cart(cart, "Headphones", 3)
print("After Adding Item:", cart)

update_cart(cart, "Mobile", 5)
print("After Updating Quantity:", cart)