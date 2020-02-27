# Review exercise 1

print("The following output is for Exercise 1")
for n in range(2, 11):
    print(n)

# Review exercise 2

print("The following output is for Exercise 2")
n = 2
while n <= 10:
    print(n)
    n = n + 1

# Review exercise 3

print("The following output is for Exercise 3")

def double(n):
    n = n * 2
    return n

print("The following output is using a for loop:")
n = 2
for x in range (1,4):
    n = double(n)
    print(n)

print("The following output is using a while loop:")
x = 1
n = 2
while x <= 3:
    n = double(n)
    print(n)
    x = x + 1