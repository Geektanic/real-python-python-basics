
# Oh man, the book solution is so good, so I wanted a local copy for future refernce.

import pathlib

path = pathlib.Path.home() / "python_documents"

images = path / "images"
images.mkdir(exist_ok=True)

for a_file in path.rglob("*.*"):
    if a_file.suffix.lower() in [".png", ".jpg", ".gif"]:
        a_file.replace(images / a_file.name)