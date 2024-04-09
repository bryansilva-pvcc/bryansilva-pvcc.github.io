# Name: Bryan Silva
# Personal property tax:
#   -- Personal property tax rate: 4.20% per year
#   -- Personal property is paid every six months, so bill should be for six months, not for the entire year
# Personal Property Tax Relief (PPTR): Some vehicles are eligible for tax relief:
#   -- Eligibility:  Owned or leased vehicles which are predominately used for non-business purposes & have 
#       passenger license plates. (These vehicles do not have to pay a license fee.)
#   -- Tax relief for qualified vehicles is 33%

import datetime

PPT_RATE = .042
RELIEF_RATE = .33

tax_due = 0
assessed_value = 0
relief_amount = 0
annual_tax_amount = 0
six_month_tax = 0
pptr_eligible = ""

def main():
    more = True
    while more:
        get_user_data()
        perform_calculation()
        display_results()

        yesno = input("\nWould you like to calculate tax fees for another car? (Y/N): ")
        if yesno == "n" or yesno == "N":
            more = False
            break

def get_user_data():
    global assessed_value, pptr_eligible
    assessed_value = float(input("Enter the assessed value of your vehicle: "))
    pptr_eligible = input("Is the vehicle eligible for tax releif? (Y/N): ")

def perform_calculation():
    global tax_due, relief_amount
    annual_tax_ammount = assessed_value * PPT_RATE
    six_month_tax = annual_tax_ammount / 2

    if pptr_eligible.upper() == "Y":
        relief_amount = six_month_tax * 0.33
    else:
        relief_amount = 0

    tax_due = six_month_tax - relief_amount
    

def display_results():
    moneyf = '8,.2f'
    line = ("----------------------------------------------------------------------")

    print(line)
    print("****************** PERSONAL PROPERTY TAX REPORT ******************")
    print("                    Charlottesville, Virginia")

    print("\n\tRUN DATE/TIME: " + str(datetime.datetime.now()))
    print("\nAccessed Value:       $ " + format(assessed_value,moneyf))
    print("Full Annual Amount:    $ " + format(tax_due * 2,moneyf))
    print("Relief Amount:         $ " + format(relief_amount,moneyf))
    print(line)
    print("************************************* Total Due:             $" + format(tax_due,moneyf))

main()