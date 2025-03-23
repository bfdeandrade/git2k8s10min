import random

friends = ["Alice", "Bob", "Charlie", "David", "Eve"]

def pick_random_friend():
    return random.choice(friends)

print(pick_random_friend())
