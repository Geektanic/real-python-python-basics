# 12.4 - Challenge.py

import pathlib

# The challenge is to move all .png, .gif, and .jpg files from their
# source inside of a cluster of directories and into a singular location

# This is my original attempt, and it worked just fine.

path = pathlib.Path.home() / "python_documents"

images = path / "images"
images.mkdir(exist_ok=True)

for pngpath in path.rglob("*.png"):
    if pngpath.parent.name != "images":
        pngpath.replace(images / pngpath.name)

for gifpath in path.rglob("*.gif"):
    if gifpath.parent.name != "images":
        gifpath.replace(images / gifpath.name)

for jpgpath in path.rglob("*.jpg"):
    if jpgpath.parent.name != "images":
        jpgpath.replace(images / jpgpath.name)