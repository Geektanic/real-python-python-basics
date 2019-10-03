# Review exercise 1
"""
number = input("Enter a number: ")
print(number + " rounded to 2 decimal places is " + str(round(float(number), 2)))
"""

# Review exercise 2
"""
number = input("Enter a number: ")
print("The absolute value of " + number + " is " + str(abs(float(number))))
"""

# Review exercise 3
"""
firstNumber = input("Enter a number: ")
secondNumber = input("Enter a number: ")
checkNumber = float(firstNumber) - float(secondNumber)
print("The difference between " + firstNumber + " and " + secondNumber + " is an integer? " + str(checkNumber.is_integer()) + "!")
"""

# Review exercise 3 from the online solutions
# Because it's way cooler than mine

num1 = float(input("Enter a number: "))

num2 = float(input("Enter another number: "))

print(

    f"The difference between {num1} and {num2} is an integer? "

    f"{(num1 - num2).is_integer()}!"
)