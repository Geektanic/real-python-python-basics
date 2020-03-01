
import pathlib

# Review question 1
# Writing some Star Trek ship names to a file in the home directory

path = pathlib.Path.home() / "starships.txt"

ships = ["Discovery\n", "Enterprise\n", "Defiant\n", "Voyager\n"]

print("Creating a new text file, starships.txt, in home directory.")

with path.open(mode="w", encoding="utf-8") as the_file:
    for ship in ships: # Book solution was just simply 'file.writelines(starships)'
        the_file.write(ship)

# Review question 2
# Reading back the newly created starships.txt, ensuring no blank lines between items

print("\nThe following items were written to the new file:")

with path.open(mode="r", encoding="utf-8") as the_file:
    for line in the_file.readlines():
        print(line, end="")


# Review question 3
# Reading back starships.txt, but only outputing ships that start with the letter D

print("\nOnly the following starships start with the letter D:")

with path.open (mode="r", encoding="utf-8") as the_file:
    for line in the_file.readlines():
        if line[0] == "D": # Book solution used 'starship.startswith("D")'
            print(line, end="")