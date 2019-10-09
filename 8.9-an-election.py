# Two candidates are running for mayor in a city with three voting regions.
# Write a program that simulates the election 10,000 times and prints the
# percentage where Candiate A wins.  A candiate wins when they win two
# of the three regions.

# Candiate A polling numbers:
# Region 1: 87% chance of winning
# Region 2: 65% chance of winning
# Region 3: 17% chance of winning

import random

def check_region_one():
    if random.random() <= 0.87:
        return 1
    else:
        return 0

def check_region_two():
    if random.random() <= 0.65:
        return 1
    else:
        return 0

def check_region_three():
    if random.random() <= 0.17:
        return 1
    else:
        return 0

def simulate_election():
    result = check_region_one() + check_region_two() + check_region_three()
    return result

wins = 0

for elections in range(10_000):
    if simulate_election() >= 2:
        wins += 1

win_percentage = (wins / elections) * 100

print(f"Our candidate won {win_percentage:.2f}% of the simulations.")