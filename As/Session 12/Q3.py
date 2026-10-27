# 3.
# Given a list of song durations in minutes, use a lambda function with the map() function to convert all durations to seconds and print the resulting list.


# Song durations in minutes
durations = [3, 4, 5, 2, 6]

# Convert minutes to seconds using lambda and map()
seconds = list(map(lambda x: x * 60, durations))

print("Song Durations in Minutes:", durations)
print("Song Durations in Seconds:", seconds)