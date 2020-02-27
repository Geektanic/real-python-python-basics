# Review exercise 1
# Trying to figure out the result of some expressions
# Comments after will be my guess

print("Start of Review Exercise 1")
x = (1 <= 1) and (1 != 1)
print(x)
# False - left is True, right is False, so True and False equal False.

x = not (1 != 2)
print(x)
# False - (1 != 2) should be True, but the not in front will make the overall result False.

x = ("good" != "bad") or False
print(x)
# True - The strings don't match, so True, and a True or False shoudl result in True.

x = ("good" != "Good") and not (1 == 1)
print(x)
# False - Strings on the left are not equal, so True on left, then 1 does equal 1, but combined with a not
# we should get False on the right.  True and False should result in False

# After running the above review it looks like I was correct - I hope for the right reasons.

# Review exercise 2
# Another exercise where you're provided code.  In this case you are to supply proper parantheses
# in order to make each expression evaluate to True.

print("Start of Review Exercise 2")
# False == not True
x = False == (not True)
print(x)
# There was an example exactly in the book like this, and because of precedence you need
# to wrap that because we can't do False == not, which is what it will try to do first.
# That's how I understood things anyway.

# True and False == True and False
x = (True and False) == (True and False)
print(x)
# It looks like just wrapping each side of == should result in an evaluation of
# False == False, which should return True.

# not True and "A" == "B"
x = not (True and "A" == "B")
print(x)
# I couldn't figure this one out, and I'm still not 100% sure why it doesn't work as
# is, or why it doesn't return True when you just wrap the right side of the and.
# I honestly didn't even think to wrap it all to turn into False, and then rely on
# not to invert that.

# Coming back to this on 11/04/2019 while just doing some general clean up of everything,
# and this makes sense now.  I see how it should evaluate to False in the (), and that would
# invert to True with the "not" in front of it.

# "B" and not "A" != "B"
x = ("B" and not "A") != "B"
print(x)
# I had zero idea what was going on here, and still haven't wrapped my head around what the
# "not "A"" is doing here.  I'll need to probably read some more on that if there's no decent
# explanation in the book.

# Coming back to this on 11/04/2019, and while I'm not 100% sure on this, I think I'm getting that
# the first section in () essentially results in something, and that something would be "True" or "False"
# (and I'm leaning to...true, because B is not A?), which doesn't truthfully evalutate as a string "B"
# But since whatever it is does not equal string "B," then it's true!