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