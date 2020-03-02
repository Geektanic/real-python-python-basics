# Had some real trouble with this one.  The text seemed to have
# some major errors in it (early access, go figure).  I did my best
# to seek out proper usage of some of these items.  Writing headers to a CSV,
# for example, was definitely funky and not working as written.

import pathlib
import csv

# Review question 1
# Writing a list of lists to a csv in home directory

numbers = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
]

file_path = pathlib.Path.home() / "numbers.csv"
with file_path.open(mode = "w", encoding = "utf-8", newline="") as the_file:
    writer = csv.writer(the_file)
    writer.writerows(numbers)

the_file.close()

# Review question 2
# Reading newly created numbers.csv and printing a list of lists

numbers = []

with file_path.open(mode = "r", encoding="utf-8", newline="") as the_file:
    reader = csv.reader(the_file)
    for row in reader:
        int_row = [int(value) for value in row]
        numbers.append(int_row)
    
the_file.close()

print(numbers)

# Review question 3
# Writing a list of dictionaries to a file

favorite_colors = [
    {"name": "Joe", "favorite_color": "blue"},
    {"name": "Anne", "favorite_color": "green"},
    {"name": "Bailey", "favorite_color": "red"},
]

headers = ["name", "favorite_color"]

file_path = pathlib.Path.home() / "employees.csv"
with file_path.open(mode="w", encoding="utf-8", newline="") as the_file:
    writer = csv.DictWriter(the_file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(favorite_colors)

the_file.close()

# Review question 4
# Reading the data from the CSV created in Q3 and puts into a list of dictionaries.

favorite_colors = []

with file_path.open(mode="r", encoding="utf-8", newline="") as the_file:
    reader = csv.DictReader(the_file)
    for row in reader:
        favorite_colors.append(row)

the_file.close()

print(favorite_colors)

# The book called for the printout to be stricly the file's contents.
# However, I can't replicate that and always get an "OrderedDict" in front of each dictionary.
# Looking around online makes it seem like that is normal for Python 3.7 (since 3.6, if I'm reading correctly).
# I'm calling this done.