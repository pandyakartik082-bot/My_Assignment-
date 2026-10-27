# 3.
# Write a function display_friends() that takes a dictionary of Instagram usernames as keys and their follower counts as values, and prints each username with their followers in the format: 'username: 2.3K followers'.


def display_friends(friends):
    for username, followers in friends.items():
        print(f"{username}: {followers / 1000:.1f}K followers")


friends = {
    "kartik_082": 2300,
    "tusu_123": 4500,
    "rahul_456": 1200
}

display_friends(friends)