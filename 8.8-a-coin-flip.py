# Challenge is to write a simulation that will flip a coin until both heads and tails
# is flipped, keeping track of the number of flips.  The simulation should run that 
# trial 10,000 times and report the average number of flips per trial.

import random

def coin_flip():
    if random.randint(0, 1) == 0:
        return "heads"
    else:
        return "tails"

def the_trial():
    heads_count = 0
    tails_count = 0
    number_of_flips = 0
    while (heads_count * tails_count) == 0:
        number_of_flips = number_of_flips + 1
        if coin_flip() == "heads":
            heads_count = heads_count + 1
        else:
            tails_count = tails_count + 1
    return number_of_flips

total_flips = 0

for trials in range(10_000):
    total_flips = total_flips + the_trial()

avg_flips = total_flips / 10_000
print(f"Average number of flips was {avg_flips:.2f}.")