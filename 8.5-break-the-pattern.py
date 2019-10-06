# Review exercise 1

while True:
    letter = input("Enter a letter: ")
    if letter.upper() == "Q":
        break

print("You entered the correct letter!")

# Review exercise 2

for n in range(1, 51):
    if n % 3 == 0:
        continue
    else:
        print(f"{n} is not a multiple of 3")