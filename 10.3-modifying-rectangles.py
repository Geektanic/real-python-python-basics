# Taking Review Exercise 2 - rectangles - and modifying it a bit.

class Rectangle:
    def __init__(self, length, width, shape):
        self.length = length
        self.width = width
        self.shape = shape

    def area(self):
        return f"The area of your {self.shape} is {self.length * self.width}."

class Square(Rectangle):
    def __init__(self, side_length, shape):
        super().__init__(side_length, side_length, shape)

length = int(input("Please enter the length of your rectangle: "))
width = int(input("Please enter the width of your rectangle: "))

if length == width:
    a_square = Square(length, "square")
    print(f"You have defined a {a_square.shape}.")
    print(a_square.area())
else:
    a_rectangle = Rectangle(length, width, "rectangele")
    print(f"You have defined a {a_rectangle.shape}.")
    print(a_rectangle.area())