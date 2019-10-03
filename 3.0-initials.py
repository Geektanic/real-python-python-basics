userFirstName = input("Please enter your first name: ")
userMiddleName = input("\nPlease enter your middle name: ")
userLastName = input("\nPlease enter your last name: ")
userFirstInitial = userFirstName[0].upper()
userMiddleInitial = userMiddleName[0].upper()
userLastInitial = userLastName[0].upper()
userInitials = userFirstInitial + userMiddleInitial + userLastInitial
print("\nYour initials are:", userInitials)

# Just looking to change something.