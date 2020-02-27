# main.py

# First Method

# import mypackage.module1
# import mypackage.module2

# mypackage.module1.greet("Pythonista")
# mypackage.module2.depart("Pythonista")

# Second method

# from mypackage import module1, module2

# module1.greet("Pythonista")
# module2.depart("Pythonista")

# Using package and subpackage

from mypackage.module1 import greet
from mypackage.mysubpackage.module3 import people

for person in people:
    greet(person)