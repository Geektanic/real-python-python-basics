# Review 1

class Dog():
    species = "Canis familiaris"

    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    # Instance method
    def __str___(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

buddy = Dog("Buddy", 9, "black")
miles = Dog("Miles", 4, "blonde")
philo = Dog("Philo", 5, "brown")

print(f"{philo.name}'s coat is {philo.coat_color}")

# Review 2 -- setup the Car() class, and then worked with blue and red car
# Review 3 -- Added .drive method to Car(), and then worked with new car and verified .drive worked

class Car():
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
    
    def drive(self, miles):
        return self.mileage + miles

blue_car = Car("blue", 20000)
red_car = Car("red", 30000)

# I just did two print lines...

# print(f"The {blue_car.color} car has {blue_car.mileage:,.0f} miles.")
# print(f"The {red_car.color} car has {red_car.mileage:,.0f} miles.")

# ...but I like the book solution better, so have included it here.

for car in (blue_car, red_car):
    print(f"The {car.color} car has {car.mileage:,.0f} miles.")

new_car = Car("purple", 0)

# Just like before, I ran three different print lines to test my .drive method...

# print(new_car.drive(100))
# print(blue_car.drive(100))
# print(red_car.drive(100))

# ...but adding this last section to use same concept from above loop.

for car in (blue_car, red_car, new_car):
    print(f"If you were to drive {car.color} car 100 miles, the mileage on the car would be {car.drive(100):,.0f} miles.")