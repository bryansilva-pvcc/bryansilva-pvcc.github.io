# Name: Bryan Silva
# Prog Purpose: This program computes PVCC college tuition & fees based on number of credits
# PVCC Fee Rates are from: https://www.pvcc.edu/tuition-and-fees

import datetime

RATE_TUITION_IN = 159.61
RATE_TUITION_OUT = 336.21
RATE_CAPITAL_FEE = 23.50
RATE_INSTITUTION_FEE = 1.75
RATE_ACTIVITY_FEE = 2.90

inout = 1    #1 means in-state, 2 means out-of-state
numcredits = 0
scholoarship_amt = 0

tuition_amt = 0
inst_fee = 0
cap_fee = 0
act_fee = 0
total = 0
balance = 0

outfile = 'tuition-webpage.html'

def main():

    open_outfile()

    more = True
    while more: 
        get_user_data()
        perform_calculations()
        create_output_file()

        yesno = input("\nWould you like to calculate tuition & fees for another student? (Y/N): ")
        if yesno == "n" or yesno == "N":
            more = False
            print("Thank you for enrolling at PVCC. Enjoy the semester!" + outfile)
            f.write('</body></html')
            f.close()

def open_outfile():
    global f
    f = open(outfile, 'w')
    f.write('<html> <head> <title> PVCC Tuitions Costs </title>\n')
    f.write('<style> td{text-align: right} </style> </head>\n')
    f.write('<body style ="background-color: #985b45; background-image: url(wp-tuition.jpg); color: #0445a0;;">\n')

def get_user_data():
    global inout, numcredits, scholoarship_amt
    print('**** PIEDMONT VIRGINIA COMM COLLEGE Tuetion & Fees ****')
    inout = int(input("Enter a 1 for IN_STATE; enter a 2 for OUT-OF-STATE: "))
    numcredits = int(input("Number of credits registered for: "))
    scholoarship_amt = int(input("Scholarship amount received: "))


def perform_calculations():
    global tuition_amt, inst_fee, cap_fee, act_fee, total, balance

    if inout == 1: 
        tuition_amt = numcredits * RATE_TUITION_IN
        cap_fee = 0
    else:
        tuition_amt = numcredits * RATE_TUITION_OUT
        cap_fee = numcredits * RATE_CAPITAL_FEE
    
    inst_fee = RATE_INSTITUTION_FEE * numcredits
    act_fee = RATE_ACTIVITY_FEE * numcredits
    total = tuition_amt + inst_fee + cap_fee + act_fee
    balance = total - scholoarship_amt


def create_output_file():
    currency = '8,.2f'
    today = str(datetime.datetime.now())
    day_time = today[0:16]

    tr = '<tr><td>'
    endtd = '</td><td>'
    endtr = '</td></tr>\n'
    colsp = '<tr><td colspan= "3">'
    sp = " "

    f.write('\n<table border="3"   style ="background-color: rgba(245, 245, 245, 0.746);  font-family: arial; margin: auto;">\n')   
    f.write(colsp + '\n')
    f.write('<h2>PIEDMONT VIRGINIA COMMUNITY COLLAGE</h2></td></tr>')
    f.write(colsp + '\n')
    f.write('------------------Tuition and Fees Report------------------\n')

    f.write(tr + 'Tuition' + endtd + format(tuition_amt,currency) + endtr)
    f.write(tr + 'Captial Fee'+ endtd + format(cap_fee,currency) + endtr)
    f.write(tr + 'Institutional Fee' + endtd + format(inst_fee,currency) + endtr)
    f.write(tr + 'Student Activity Fee' + endtd + format(act_fee,currency) + endtr)

    f.write(tr + 'Total Fees' + endtd + sp + endtd + format(total, currency) + endtr)
    f.write(tr + 'Balance after Scholoarship' + endtd + sp + endtd + format(balance, currency))

    f.write(colsp + 'Date/Time: '+ day_time + endtr)
    f.write('</table><br />')


main()