# Review exercise 1

data = ((1, 2), (3, 4))
print(type(data))
print(data)

# Review exercise 2

for elements in range(len(data)):
    print(f"Row {elements + 1} sum: ", sum(data[elements]))

# Review exercise 3

numbers = [4, 3, 2, 1]
print(numbers)

# Review exercise 4

copy_numbers = numbers[:]
print(copy_numbers)

# Review exercise 5

numbers.sort()
print(numbers)