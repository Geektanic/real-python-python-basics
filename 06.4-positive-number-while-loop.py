# Modified the book example to use a function.

def aint_positive(num):
    print("That's not a positive number!")
    num = float(input("Enter a positive number: "))
    return(num)

num = float(input("Enter a positive number: "))

while num <= 0:
        num = aint_positive(num)