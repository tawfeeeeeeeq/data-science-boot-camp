'''
This program allows the user to access two different financial calculators: 
  (1) an investment calculator   
  (2) a home loan repayment calculator.
'''
import math

# Explain to the user possible inputs
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")

# This is the Finance Type chosen by the user
finance_type = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

# This is a list of all finance types this program handles
finance_types = ["bond", "investment"]

# If the user did not enter an acceptable value, print and error message and exit the program
if finance_type not in finance_types:
    print("Error: you have not entered either 'investment' or 'bond'.")
    exit()


if finance_type == "investment":
    # Request from user, (1) Amount of Money they will invest, keep trying until you get a valid response
    while True:
        try:
            invest_amount = float(input("Enter the amount of money you will invest: "))
        except ValueError:
            print("Sorry, invalid input, try again.")
            continue
        else:
            break
    # Request from user, (2) The interest rate, keep trying until you get a valid response
    while True:
        try:
            interest_rate = float(input("Enter the interest rate e.g. for `12%` please enter `12`: "))
        except ValueError:
            print("Sorry, invalid input, try again.")
            continue
        else:
            break
    # Request from user, (3) Number of years they will invest, keep trying until you get a valid response
    while True:
        try:
            invest_years = int(input("Enter the number of years you will be investing: "))
        except ValueError:
            print("Sorry, invalid input, try again.")
            continue
        else:
            break
    # Request from user, (4) Interest type `simple` or `compound`, keep trying until you get a valid response
    while True:
        interest = input("Enter type of interest you require, either `simple` or `compound`: ").lower()
        if (interest == "simple" or interest == "compound"):
            break
        else:
            print("Sorry, invalid input, try again.")

    # Find out what the investment return is depending on whether the user chose `simple` or `compound`
    if interest == "simple":
        invest_return = invest_amount * (1 + (interest_rate/100)*invest_years)
    elif interest == "compound":
        invest_return = invest_amount * math.pow((1+(interest_rate/100)),invest_years)

    # Print the details of the investment along with the final return
    print("Ininital Investment: ", invest_amount)
    print("Interest Rate: ", interest_rate)
    print("Interest Type: ", interest)
    print("Number of years: ", invest_years)
    print("Total Return: ", invest_return)

elif finance_type == "bond":
    # Request from user, (1) The present value of their house, keep trying until you get a valid response
    while True:
        try:
            house_value = float(input("Enter the present value of the house: "))
        except ValueError:
            print("Sorry, invalid input, try again.")
            continue
        else:
            break
    # Request from user, (2) The interest rate, keep trying until you get a valid response
    while True:
        try:
            interest_rate = float(input("Enter the interest rate e.g. for `12%` please enter `12`: "))
        except ValueError:
            print("Sorry, invalid input, try again.")
            continue
        else:
            break
    # Request from user, (3) The number of months they plan to take to repay the bond, keep trying until you get a valid response
    while True:
        try:
            repay_months = int(input("Enter number of months you plan to take to repay the bond: "))
        except ValueError:
            print("Sorry, invalid input, try again.")
            continue
        else:
            break

    # Calculate the monthly repayment amount
    repayment = ((interest_rate/100/12) * house_value)/(1 - (1 + (interest_rate/100/12))**(-repay_months))

    # Print the details of the bond along with the Monthly repayment amount
    print("Present house value: ", house_value)
    print("Interest Rate: ", interest_rate)
    print("Repayment Months: ", repay_months)
    print("Monthly Repayments: ", repayment)