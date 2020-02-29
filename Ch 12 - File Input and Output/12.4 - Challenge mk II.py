# 12.4 - Challenge mk II.py

import pathlib

# The challenge is to move all .png, .gif, and .jpg files from their
# source inside of a cluster of directories and into a singular location

# After finishing the first attempt I realized I could probably build a function
# to do the actual find and move.  I didn't want to lose my original work, 
# so here we go.

path = pathlib.Path.home() / "python_documents"

images = path / "images"
images.mkdir(exist_ok=True)

def find_and_copy(ext):
    for the_file in path.rglob(f"*.{ext}"):
        if the_file.parent.name != "images":
            the_file.replace(images / the_file.name)

extensions = ["png", "gif", "jpg"]

for ext in extensions:
    find_and_copy(ext)