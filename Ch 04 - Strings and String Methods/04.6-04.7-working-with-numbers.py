num = input("Please enter a number to be doubled: ")
doubleNumInt = int(num) * 2
print("\nThe entered number, doubled as an integer is", doubleNumInt)
doubleNumFloat = float(num) * 2
print("\nThe entered number, double as a float is", doubleNumFloat)
print("\n\n")


numPancakes = input("How many pancakes you want? ")
print("You really gonna eat " + str(numPancakes) + " pancakes?")
print("\nOne hour later.")
numPancakesEaten = input("\nHow many pancakes did you really eat? ")
print("So I have " + str(int(numPancakes) - int(numPancakesEaten)) + " pancakes left?!?!")


numberOne = input("\nEnter a number: ")
numberTwo = input("\nEnter a second number:")
print("\nThe product of " + numberOne + " and " + numberTwo + " is " + str(float(numberOne) * float(numberTwo)))


name = input("What's your name? ")
heads = input("How many heads you got? ")
arms = input("How many arms you got? ")
print(f"{name} has {heads} heads and {arms} arms.")
print("{} has {} heads and {} arms.".format(name, heads, arms))