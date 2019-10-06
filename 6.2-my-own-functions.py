def multiply(x, y):
    product = x * y
    return product

num = multiply(2, 4)
print(num)

# Review exercise 1

def cube(x):
    """Gets a number and cubes it"""
    cubed_number = x ** 3
    return cubed_number

cubed = cube(float(input("Give us a number: ")))
print(f"That number cubed is {cubed:.2f}.")


# Review exercise 2

def greet(name):
    """Gets a string and greets that string."""
    print(f"Hello, {name}.")

greet(input("What's your name, robot slayer?\n"))