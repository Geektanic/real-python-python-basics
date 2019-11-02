# Review question 1

captains = {}
print(captains)
print(type(captains))

# Review question 2

captains["Enterprise"] = "Picard"
captains["Voyager"] = "Janeway"
captains["Defiant"] = "Sisko"
print(captains)
print(captains["Enterprise"])

# Review question 3

if "Enterprise" in captains:
    print("Captain on deck!")
else:
    captains["Enterprise"] = "unknown"

if "Discovery" in captains:
    print("Captain on deck!")
else:
    captains["Discovery"] = "Unknown (but Pike was pretty good!)"

print(captains)

# Review question 4

for captain in captains:
    print(f"The {captain} is captained by {captains[captain]}")

# Review question 5

del captains["Discovery"]
print(captains)

# Review question 6 (Bonus!)

captain_ship_pairs = (
    ("Enterprise", "Picard"),
    ("Voyager", "Janeway"),
    ("Defiant", "Sisko")
)

bonus_captains = dict(captain_ship_pairs)
print(bonus_captains)

# Playing around with it, and moving to Star Wars.

def read_out():
    print("So you're telling me:")
    for user in force_user_color_pair:
        print(f"{user[0].upper()}{user[1:].lower()} uses a {force_user_color_pair[user].lower()} lightsaber?")

def get_pairs(count):
    
    force_users = ()
    lightsaber_colors = ()
    pairings = ()
    
    while len(force_users) < count:
        force_user = input("Please enter a force user: ")
        force_users = force_users + (force_user,)
        lightsaber_color = input("Please enter the color of their ligthsaber: ")
        lightsaber_colors = lightsaber_colors + (lightsaber_color,)
        pair = (force_user, lightsaber_color)
        pairings = pairings + (pair,)
    return pairings

while True:
    try:
        number_of_users = int(input("How many force users would you like to discuss? Enter a decimal number: "))
        break
    except ValueError:
        print("Please only use numbers represented in decimal format.")
        continue

force_user_color_pair = dict(get_pairs(number_of_users))

read_out()

