# Who wins at the sports game?

def select_sport():
    test_sport = "invalid"
    while test_sport != "basketball" or "golf":
        test_sport = input("What game are you playing?\nOptions are basketball or golf: ")
    return sport

sport = select_sport()

p1_score = input("Enter Player 1 score: ")
p2_score = input("Enter Player 2 score: ")

if p1_score == p2_score:
    print("The game was a tie/draw.")

elif sport.lower() == "basketball" or sport.lower() == "golf":
    p1_wins_basketball = sport == "basketball" and p1_score > p2_score
    p1_wins_golf = sport == "golf" and p1_score < p2_score
    p1_wins = p1_wins_basketball or p1_wins_golf

    if p1_wins:
        print("Player 1 wins.")
    else:
        print("Player 2 wins.")

else:
    print("Unknown sport.")