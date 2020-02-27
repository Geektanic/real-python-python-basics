# A United State capital guessing game.

import random

capitals_dict = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento",
    "Colorado": "Denver",
    "Connecticut": "Hartford",
    "Delaware": "Dover",
    "Florida": "Tallahassee",
    "Georgia": "Atlanta",
    "Hawaii": "Honolulu",
    "Idaho": "Boise",
    "Illinois": "Springfield",
    "Indiana": "Indianapolis",
    "Iowa": "Des Moines",
    "Kansas": "Topeka",
    "Kentucky": "Frankfort",
    "Louisiana": "Baton Rouge",
    "Maine": "Augusta",
    "Maryland": "Annapolis",
    "Massachusetts": "Boston",
    "Michigan": "Lansing",
    "Minnesota": "Saint Paul",
    "Mississippi": "Jackson",
    "Missouri": "Jefferson City",
    "Montana": "Helena",
    "Nebraska": "Lincoln",
    "Nevada": "Carson City",
    "New Hampshire": "Concord",
    "New Jersey": "Trenton",
    "New Mexico": "Santa Fe",
    "New York": "Albany",
    "North Carolina": "Raleigh",
    "North Dakota": "Bismarck",
    "Ohio": "Columbus",
    "Oklahoma": "Oklahoma City",
    "Oregon": "Salem",
    "Pennsylvania": "Harrisburg",
    "Rhode Island": "Providence",
    "South Carolina": "Columbia",
    "South Dakota": "Pierre",
    "Tennessee": "Nashville",
    "Texas": "Austin",
    "Utah": "Salt Lake City",
    "Vermont": "Montpelier",
    "Virginia": "Richmond",
    "Washington": "Olympia",
    "West Virginia": "Charleston",
    "Wisconsin": "Madison",
    "Wyoming": "Cheyenne",
}

# I figured out the following method first:

"""
state = random.choice(list(capitals_dict))
capital = capitals_dict[state]
"""

# I like the look of this method, which I figured out second:
def the_pick():
    state, capital = random.choice(list(capitals_dict.items()))
    return state, capital
    
def the_game(number_of_guesses, state, capital):
    guess = ""

    while guess.lower() != capital.lower():
        guess = input(f"What is the capital of {state}? ")
        if guess.lower() == "exit":
            print(f"Good guessing. The answer was {capital}.")
            exit_value = 0
            return exit_value, number_of_guesses
        else:
            number_of_guesses = number_of_guesses + 1
    else:
        print("Correct!")
        exit_value = 1
        return exit_value, number_of_guesses


print("You're going to play a guessing game, in which you must supply the capital city of a given state.")
print("You may guess as many times as you like. As long as you are correct, you will keep playing.")
print("If you would like to give up at any time simply type 'exit'.")

exit_value = 1
number_correct = 0
number_of_guesses = 0

while exit_value == 1:
    state, capital = the_pick()
    exit_value, number_of_guesses = the_game(number_of_guesses, state, capital)
    if exit_value == 1:
        number_correct = number_correct + 1

print(f"You guessed {number_of_guesses} times, and got {number_correct} correct. Thanks for playing!")
