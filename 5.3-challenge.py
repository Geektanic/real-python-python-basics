# Version 1.0
# This is just the first way I thought of how to do the challenge.

firstNumber = input("Please enter a base number: ")
secondNumber = input("Please enter an exponent: ")
print(firstNumber + " raised to the power of " + secondNumber + " = " + str(float(firstNumber) ** float(secondNumber)))


# Version 2.0
# No clue if this is "better," but wanted to try an f-string

print("")
endProduct = float(firstNumber) ** float(secondNumber)
print(f"{firstNumber} raised to the power of {secondNumber} = {endProduct}")