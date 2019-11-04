# Two candidates are running for mayor in a city with three voting regions.
# Write a program that simulates the election 10,000 times and prints the
# percentage where Candiate A wins.  A candiate wins when they win two
# of the three regions.

import random

def check_a_region(region_chances):
    if random.random() <= region_chances:
        return 1
    else:
        return 0

region_one_chances = int(input("What percentage does your candiate have in Region One? ")) * .01
region_two_chances = int(input("What percentage does your candidate have in Region Two? ")) * .01
region_three_chances = int(input("What percentage does your candidate have in Region Three? ")) * .01

wins = 0

for elections in range(10_000):
    if check_a_region(region_one_chances) + check_a_region(region_two_chances) + check_a_region(region_three_chances) >= 2:
        wins += 1

win_percentage = (wins / elections) * 100

print(f"Our candidate won {win_percentage:.2f}% of the simulations.")