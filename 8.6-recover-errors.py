# Review exercise 1

while True:
    try:
        num = input("Enter an integer:")
        print(int(num))
        break
    except ValueError:
        print("Try again.")

# Review exercise 2

string = input("Give us a string: ")

try:
    n = int(input("Give us an integer: "))
    print(string[n])
except ValueError:
    print("Invalid number.")
except IndexError:
    print("Invalid index.")