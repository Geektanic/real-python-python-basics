# Code produced while following along with the chapter.

"""class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def __str__(self):
        return(f"{self.name} is {self.age} years old.")

    def speak(self, sound):
        return f"{self.name} says {sound}."

miles = Dog("Miles", 4, "Jack Russell Terrier")
buddy = Dog("Buddy", 9, "Dachshund")
jack = Dog("Jack", 3, "Bulldog")
jim = Dog("Jim", 5, "Bulldog")"""

# print(miles)

# print(miles.speak("yap"))
# print(jim.speak("woof"))
# print(jack.speak("woof"))

# for dog in (miles, buddy, jack, jim):
#     print(dog.speak("lolol"))

# list_of_dogs = [miles, buddy, jack, jim]

# for dog in list_of_dogs:
#     print(dog)

# for dog in list_of_dogs:
#     print(dog.speak("lolol list"))

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return(f"{self.name} is {self.age} years old.")

    def speak(self, sound):
        return f"{self.name} barks {sound}."

class JackRussellTerrier(Dog):
    def speak(self, sound="arf"):
        return super().speak(sound)

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass

miles = JackRussellTerrier("Miles", 4)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)

# print(miles.species)
# print(buddy.name)
# print(jack)
# print(jim.speak("woof"))

# print(type(miles))
# print(isinstance(miles, Dog))
# print(isinstance(miles, Bulldog))

print(miles.speak())
print(miles.speak("grrr"))
print(jim.speak("woooooof"))