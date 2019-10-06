# Write a script that asks the user to input a positive integer and then
# prints out the factors of that number.

number = int(input("Enter a positive integer: "))

for n in range(1, number + 1):
    test_remainder = number % n
    if test_remainder == 0:
        print(f"{n} is a factor of {number}")

# Including book solution for future reference.

num = int(input("Enter a positive integer: "))
for divisor in range(1, num + 1):
    if num % divisor == 0:
        print(f"{divisor} is a factor of {num}")