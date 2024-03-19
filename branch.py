# Name: Bryan Silva
# Prog Purpose: This program finds the cost of a meal at Branch Barbeque Buffet
#   Price for an adult meal: $19.95
#   Price for child meal: $11.95
#   Service fee: 10%
#   Sales tax rate: 6.2%

import datetime

##############  define global variables  ##############
# define tax rate, serfice fee, and prices
ADULT_MEAL = 19.95
CHILD_MEAL = 11.95
SALES_TAX_RATE = .062
SERVICE_FEE = .10

# define glabal varialbes
num_adult_meals = 0
num_child_meals = 0
subtotal = 0
sales_tax = 0
service_fee = 0
total = 0

##############  define program functions  ##############
def main():

    more_meals = True

    while more_meals:
        get_user_data()
        perform_calculations()
        display_results()

        yesno = input("\nWould you like to order again (Y or N)? ")
        if yesno == "N" or yesno == "n":
            more_meals = False
            print("Thank you for coming to Branch Barbeque Buffet! Enjoy your meal!")

def get_user_data():
    global num_adult_meals, num_child_meals
    num_child_meals = int(input("Number of Children Meals: "))
    num_adult_meals = int(input("Number of Adult Meals: "))

def perform_calculations():
    global subtotal_child, subtotal_adult, sales_tax, service_fee, total
    subtotal_adult = num_adult_meals * ADULT_MEAL
    subtotal_child = num_adult_meals * CHILD_MEAL
    sales_tax = (subtotal_adult + subtotal_child) * SALES_TAX_RATE
    service_fee = (subtotal_adult + subtotal_child) * SERVICE_FEE
    total = subtotal_adult + subtotal_child + sales_tax + service_fee

def display_results():
    print('--------------------------------')
    print('**** Branch Barbeque Buffet ****')
    print('--------------------------------')
    print('Children Meals    $ ' + format(subtotal_child,'8,.2f'))
    print('Adult Meals       $ ' + format(subtotal_adult,'8,.2f'))
    print('Sales Tax         $ ' + format(sales_tax,'8,.2f'))
    print('Service Fee       $ ' + format(service_fee,'8,.2f'))
    print('Total             $ ' + format(total,'8,.2f'))
    print('--------------------------------')
    print(str(datetime.datetime.now()))

######## call on main program to execute #######
main()
