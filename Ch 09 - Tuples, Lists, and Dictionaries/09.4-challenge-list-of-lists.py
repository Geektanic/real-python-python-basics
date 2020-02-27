# We're given a list of lists, and then instructed to define various functions
# and do various things.

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

print("***************************************")
print(f"Total students:    {total_students:,}")
print(f"Total tuition:     ${total_tuition:,.2f}")
print(f"Student mean:      {mean_students:,.0f}")
print(f"Student median:    {median_students:,}")
print(f"Tuition mean:      ${mean_tuition:,.2f}")
print(f"Tutition median:   ${median_tuition:,}")
print("***************************************")