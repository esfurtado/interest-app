# The following code will use a finance calculator which will change according to the user's choices of what they wish to calculate.

import math

amount = 0 # This variable will assume the resulting total of interest to be earned by the user when they want to calculate "investment"

loan = 0 # This will assume the total repayment money for each month when the user selects "bond"

money = 0 # Variable created to assume the either the amount of money initially invested by the user or the price of the house they want to invest in.

rate = 0 # Variable to assume the rate that the user either wants to apply to the investment or to the bond

time = 0 # Variable to assume either the time in years or months depending on the calculator the user selected

interest = "" # For "investment" this variable will either assume the value of "simple" or "compound"


product = input(''' Choose either 'investment' or 'bond' from the menu below to proceed:\n
investment\t- to calculate the amount of interest you'll earn on interest\n
bond\t- to calculate the amount you'll have to pay on a home loan\n''').lower()

if product == "investment":
    print("You have selected investement.")

    money = float(input("How much money are you depositing? "))
    rate = float(input("What interest rate will be applied to your investment? "))
    time = int(input("For how many years will you be investing? "))
    interest = input("Please select whether you prefer 'compound' or 'simple' interest: ").lower()

    if interest == "simple":
        amount = int(money*(1 + (rate/100) * time))
    elif interest == "compound":
        amount = int(money* math.pow((1 + (rate/100)), time))

    print(f"For an initial investment of {money}€, with an interest rate of {rate}%, invested for {time} years you will earn a total of: {amount}€")



elif product == "bond":
    print("You have selected bond.")

    money = float(input("How much does the property cost? "))
    rate = float(input("How much interest will be applied to your loan? "))
    rate = (rate/100)/12
    time = int(input("For how many months will you be paying your loan? "))
    loan = ((rate * money)/(1 - math.pow((1+rate), (-time))))
    
    loan = round(loan, 3) # Rounding the loan results so they are easier to read

    print(f"For a property costing {money}€, being paid for a total of {time} months, you will have a monthly bond repayment of: {loan}€")


else: print ("You have not selected a valid option.")
