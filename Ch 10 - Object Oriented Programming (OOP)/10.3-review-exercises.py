# Review exercise 1

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."

    def speak(self, sound):
        return f"{self.name} says {sound}."

class GoldenRetriever(Dog):
    def speak(self, sound="bark"):
        return super().speak(sound)

pup = GoldenRetriever("Pup", 5)

print(pup)
print(pup.speak())

# Review exercise 2

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return f"The area of your rectangle is {self.length * self.width}."

# I did the following:

"""class Square(Rectangle):
    def __init__(self, side_length):
        self.length = side_length
        self.width = side_length"""

# The book solution:

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

length = int(input("Please enter the length of your rectangle: "))
width = int(input("Please enter the width of your rectangle: "))

the_rectangle = Rectangle(length, width)

print(the_rectangle.area())

the_square = Square(4)

print(the_square.area())