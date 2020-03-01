
import pathlib

# Review question 1
# Setting a path to a file in home directory

# file_path = pathlib.Path(r"C:\Users\<<censor>>\my_folder\my_file.txt")

# Book solution is pretty good and doesn't reveal my username!

file_path = pathlib.Path.home() / "my_folder" / "my_file.txt"

# Review question 2
# Checking if path exists

print(file_path.exists())

# Review question 3
# Printing name of file path so the output reads my_file.txt

print(file_path.stem + file_path.suffix)

# Oops, I forgot the builtin method.

print(file_path.name)

# Review question 4
# Printing parent directory - should read my_folder

print(file_path.parent) # This prints the absolute path

# Setting up a new variable for the file's direcotry, and then just grabbing the .name
parent_directory = file_path.parent
print(parent_directory.name)

# Oh man, the book solutions are just so much more simple.

print(file_path.parent.name)