# Review exercise 1
# You're supposed to guess whether each expression will return True or False
# and then type them into the interactive window
# Instead I'll have a script print it out and use comments for my guesses
# Guesses come after output line

print("Start of Review Exercise 1")
print(1 <= 1)
# True - 1 is indeed less than or equal to 1
print(1 != 1)
# False - 1 is equal to 1, and this is evaluating if it is NOT equal
print(1 != 2)
# True - 1 is indeed not equal to 2
x = "good" != "bad"
print(x)
# False - those strings are not equal
# I got the above wrong, even though I think my explanation is correct
x = "good" != "Good"
print(x)
# True - those strings are not equal
x = 123 == "123"
print(x)
# False - this is tricky, but I'm guessing they aren't equal because they aren't even the same type

# Five out of six isn't bad!

# Review exercise 2
# This is a fill in the blank
# I'm using the following commented code to show what you were supplied with

# 3 _ 4
# 10 _ 5
# "jack" _ "jill"
# 42 _ 42

# You're supposed to fill in the blank so that the expression would evaluate to "True"

print("Start of Review Exercise 2")
print(3 < 4)
print(10 > 5)
x = "jack" != "jill"
print(x)
x = 42 != "42"
print(x)

# Heeey, got that first try, even though a few have multiple correct options.