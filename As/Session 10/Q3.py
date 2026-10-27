# 3.
# Try to change the first element of your fav_apps tuple to 'YouTube' and observe the error message. Write a comment explaining why this happens based on tuple immutability.


fav_apps = ("Instagram", "Zomato", "Spotify", "WhatsApp", "Flipkart")

print("Original Tuple:", fav_apps)

# Trying to change the first element of the tuple
fav_apps[0] = "YouTube"

# Tuples are immutable in Python.
# This means we cannot change, add, or remove
# individual elements after creating a tuple.
# Therefore, Python raises a TypeError.