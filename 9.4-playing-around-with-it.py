# We're given a list of lists, and then instructed to define various functions
# and do various things to summarize some data.

def enrollment_stats(a_list):
    enrollment = []
    tuition_fees = []
    for elements in a_list:
        enrollment.append(elements[1])
        tuition_fees.append(elements[2])
    return enrollment, tuition_fees


def mean(a_list):
    return sum(a_list) / len(a_list)

def median(a_list):
    a_list.sort()
    length = len(a_list)
    if not length % 2:
        return a_list[(length -1 ) / 2]
    return a_list[int(length / 2)]

universities = [
    ["California Institute of Technology", 2175, 37704],
    ["Harvard", 19627, 39849],
    ["Massachusetts Institute of Technology", 10566, 40732],
    ["Princeton", 7802, 37000],
    ["Rice", 5879, 35551],
    ["Stanford", 19535, 40569],
    ["Yale", 11701, 40500],
]

totals = enrollment_stats(universities)
total_students = sum(totals[0])
total_tuition = sum(totals[1])
mean_students = mean(totals[0])
median_students = median(totals[0])
mean_tuition = mean(totals[1])
median_tuition = median(totals[1])

# The following loop lists out the universities and their details before giving the summaries.
# This is not in the original program, I just added it for kicks and giggles.

counter = 0

for items in universities:
    print(f"The university, {universities[counter][0]}, has {universities[counter][1]:,} students, with an average tuition of ${universities[counter][2]:,.2f}.")
    counter = counter + 1

# The summary "table" below is a part of the base program.

print("***************************************")
print(f"Total students:    {total_students:,}")
print(f"Total tuition:     ${total_tuition:,.2f}")
print(f"Student mean:      {mean_students:,.0f}")
print(f"Student median:    {median_students:,}")
print(f"Tuition mean:      ${mean_tuition:,.2f}")
print(f"Tutition median:   ${median_tuition:,}")
print("***************************************")

# The rest of the code is an attempt to change program behavior to ask for the initial data.
# This is being done just for the fun of it, and see if I can pull it off with the skillset I have at the time of typing.

while True:
    try:
        uni_amount = int(input("How many universities are we working with today, human? "))
    except ValueError:
        print("Please enter a whole number using decimal notation.")
        continue
    break

uni_list = []
uni_counter = 0
while uni_counter < uni_amount:
    new_uni = input("Please enter a university to add to the list: ")
    uni_list.append(new_uni)
    uni_counter = uni_counter + 1

uni_enroll_list = []
enroll_counter = 0
while enroll_counter < uni_amount:
    new_enroll = input(f"Please enter {uni_list[enroll_counter]}\'s total enrollment: ")
    uni_enroll_list.append(new_enroll)
    enroll_counter = enroll_counter + 1

uni_tuition_list = []
tuition_counter = 0
while tuition_counter < uni_amount:
    new_tuition = input(f"Please enter {uni_list[tuition_counter]}\'s average tuition: ")
    uni_tuition_list.append(new_tuition)
    tuition_counter = tuition_counter + 1

print(uni_list)
print(uni_enroll_list)
print(uni_tuition_list)