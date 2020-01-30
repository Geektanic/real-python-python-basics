# We gonna throw some classes at the wall and see what sticks!

class Animal:
    def __init__(self, name, sex, age, num_legs, color):
        self.name = name
        self.sex = sex
        self.age = age
        self.num_legs = num_legs
        self.color = color

    def speak(self, sound):
        return f"{self.name} says {sound}."

class Cow(Animal):
    def __init__(self, name, sex, age, num_legs, color, spots, dairy_or_slaughter):
        super().__init__(name, sex, age, num_legs, color)
        self.spots = spots
        self.dairy_or_slaughter = dairy_or_slaughter

    def ready(self, milk_or_slaughter):
        if self.dairy_or_slaughter == "dairy":
            return f"{self.name} is ready for milking."
        else:
            return f"{self.name} is ready for slaughter."

class Horse(Animal):
    def __init__(self, name, sex, age, num_legs, color, riding_or_show):
        super().__init__(name, sex, age, num_legs, color)
        self.riding_or_show = riding_or_show

    def location(self, location):
        return f"{self.name} is in the {self.location}."

class Pig(Animal):
    def __init__(self, name, sex, age, num_legs, color, foodtype):
        super().__init__(name, sex, age, num_legs, color)
        self.foodtype = foodtype

    def activity(self, activity):
        return f"{self.name} is currently {self.activity}."

class Chicken(Animal):
    def __init__(self, name, sex, age, num_legs, color, eggs):
        super().__init__(name, sex, age, num_legs, color)
        self.eggs = eggs

    def location(self, location):
        return f"{self.name} is in the {self.location}."


# Time to make up some kind of scenario(s) that might utilize the above stuff.
# Let's see what happens!

animals = ["Cow", "Horse", "Pig", "Chicken"]
animal = "Not here"

print("Welcome to the farm!")
print("We accept cows, horses, pigs, and chickens.")

while animal not in animals:
    animal = input("Which type of animal would you like to bring to the farm? ").lower().capitalize()
    if animal in animals:
        break
    print("We don't accept that type of animal. Please come back with a cow, horse, pig, or chicken.")

new_name = input(f"What is this {animal}'s name? ").lower().capitalize()
new_sex = input(f"What is this {new_name}'s sex? ")
new_age = input(f"What is this {new_name}'s age? ")
new_num_legs = input(f"How many legs does {new_name} have? ")
new_color = input(f"What single color would use to describe {new_name}? ").lower()
new_spots = input(f"Does {new_name} have spots? ").lower()
new_dairy_or_slaughter = input(f"Is {new_name} for dairy or slaughter? ").lower()

the_animal = Cow(new_name, new_sex, new_age, new_num_legs, new_color, new_spots, new_dairy_or_slaughter)

print("----------------------------------------------------------------------------")
print(f"To review, the animal you brought today, {the_animal.name}, is a {the_animal.age} year old, {the_animal.sex.lower()} {animal.lower()}.")

if the_animal.spots == "yes":
    print(f"{the_animal.name} is also a {the_animal.color}, {the_animal.num_legs} legged, {the_animal.dairy_or_slaughter} cow with spots.")
else:
    print(f"{the_animal.name} is also a {the_animal.color}, {the_animal.num_legs} legged, {the_animal.dairy_or_slaughter} cow without spots.")

print("----------------------------------------------------------------------------")
print("---------------------------TWO WEEKS LATER----------------------------------")
print("----------------------------------------------------------------------------")

print(the_animal.ready(the_animal.dairy_or_slaughter))