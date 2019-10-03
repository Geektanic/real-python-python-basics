# 6.3 Challenge is to write a script for temperature conversion
# The focus of the chapter is functions

def convert_cel_to_far(given_cel):
    converted_far = given_cel * 9/5 + 32
    return(converted_far)

def convert_far_to_cel(given_far):
    converted_cel = (given_far - 32) * 5/9
    return(converted_cel)

given_far = float(input("Give us a temperature in F: "))
converted_cel = convert_far_to_cel(given_far)
print(f"{given_far} degrees F is {converted_cel:.2f} degrees C.")

given_cel = float(input("Give us a temperature in C: "))
converted_far = convert_cel_to_far(given_cel)
print(f"{given_cel} degrees C is {converted_far:.2f} degrees F.")