# Who wins at the sports game?
# The book example was just a fairly simple example using if, elif, and else.
# I've modified it to the below code using more of what the book has taught up to this point.
# The major change is setting up functions.  That also changes the behavior of the ending if/else,
# as it was an if/elif/else statement before.

def select_sport():
    test_sport = input("What game are you playing?\nOptions are basketball or golf: ")
    if test_sport.lower() == "basketball" or test_sport.lower() == "golf":
        return test_sport
    else:
        select_sport()

def score_input(player_number):
    test_score = input(f"Enter Player {player_number} score: ")
    return test_score

sport = select_sport()

p1_score = score_input(1)
p2_score = score_input(2)

if p1_score == p2_score:
    print("The game was a tie/draw.")

else:
    p1_wins_basketball = sport == "basketball" and p1_score > p2_score
    p1_wins_golf = sport == "golf" and p1_score < p2_score
    p1_wins = p1_wins_basketball or p1_wins_golf

    if p1_wins:
        print("Player 1 wins.")
    else:
        print("Player 2 wins.")


# Review exercise 1

word = input("Please enter one word: ")

if len(word) < 5:
    print("That word is less than five letters long.")
elif len(word) > 5:
    print("That word is greater than five letters long.")
else:
    print("That word is five letters long.")