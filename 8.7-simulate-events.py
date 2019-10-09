import random

def coin_flip_output(type_of_flip):
    print(f"Starting the {type_of_flip} coin flip process.")
    print(f"After 10,000 coin flips, we saw heads {heads_count} times, and we saw tails {tails_count} times.")

    ratio = heads_count / tails_count

    print(f"The ratio of heads to tails is {ratio:.2f}.")

def coin_flip():
    if random.randint(0, 1) == 0:
        return "heads"
    else:
        return "tails"

def unfair_coin_flip(probability_of_tails):
    if random.random() < probability_of_tails:
        return "tails"
    else:
        return "heads"

# Flipping a fair coin
heads_count = 0
tails_count = 0

for n in range(10000):
    if coin_flip() == "heads":
        heads_count = heads_count + 1
    else:
        tails_count = tails_count + 1

coin_flip_output("fair")

# Flipping an unfair coin
heads_count = 0
tails_count = 0

for trial in range(10000):
    if unfair_coin_flip(.7) == "heads":
        heads_count = heads_count + 1
    else:
        tails_count = tails_count + 1

coin_flip_output("unfair")

# Review exercise 1

def roll():
    roll = random.randint(1, 6)
    return roll

# Book solution is:
# def roll():
# return random.randint(1, 6)

print(f"You rolled a dice, and rolled a {roll()}.")

# Review exercise 2

sum_of_rolls = 0

for rolls in range(10_000):
    sum_of_rolls = sum_of_rolls + roll()

avg_roll = sum_of_rolls / rolls
print(f"You rolled 10,000 dice, and the average dice roll was {avg_roll:.2f}.")