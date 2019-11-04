# Challenge is to write an investment calculation
# I added a way for the tool to report how much money your initial invesment made

def invest(amount, rate, years):
    calculated_amount = amount + (amount * rate)
    for year in range(1, years + 1):
        print(f"Year {year}: ${calculated_amount:,.2f}")
        # The following while loop is not a part of the initial challenge
        while year == years:
            print(f"Your initial investment of ${amount:.2f} made you ${calculated_amount - amount:,.2f}!")
            year = year + 1
        calculated_amount = calculated_amount + (calculated_amount * rate)

amount = float((input("How much you depositing? ")))
rate = float((input("What rate you get? ")))
years = int((input("How many years you not touching your money? ")))
invest(amount, rate, years)