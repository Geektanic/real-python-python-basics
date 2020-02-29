# main.py

import pathlib
import shutil

# This ones a little scary. Messing with files and folders and I have made the
# bold decision to do this on my real system, not a VM.

# Review question 1
# Creating my_folder/ in home directory

my_folder = pathlib.Path.home() / "my_folder"
my_folder.mkdir(exist_ok=True)

# Review question 2
# Creating three files inside of my_folder/

file_list = ["file1.txt", "file2.txt", "image1.png"]

for file in file_list:
    file = my_folder / file
    file.touch()

# Review question 3
# Moving image1.png to a new directory my_folder/images/

images_folder = my_folder / "images"
images_folder.mkdir(exist_ok=True)

source = my_folder / "image1.png"
dest = images_folder / "image1.png"
source.replace(dest)

# Review question 4
# Deleting file1.txt

file1 = my_folder / "file1.txt"
file1.unlink()

# Review question 5
# Deleting my_folder/

shutil.rmtree(my_folder)