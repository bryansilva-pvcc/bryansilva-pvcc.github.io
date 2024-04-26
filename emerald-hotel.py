#Name: Bryan Silva
#Prog Purpose: This program reads in a hotel data file, performs calculations, and creates an HTML file for the results

import datetime

############ define rate tuples ############

#            SR  DR  SU
#             0   1   2
ROOM_RATES = (195,250,350)

#           s-tax   occ-tax
#              0      1
TAX_RATES = (0.065,0.1125)
 
########### define files and list ############
infile = "emerald.csv"
outfile = "emerald-web-page.html"

guest = [] 

############ define program functions ############
def main():
    read_in_guest_file()
    perform_calculations()
    open_out_file()
    create_output_html()
            
def read_in_guest_file():
    guest_data = open(infile, "r")
    guest_in   = guest_data.readlines()
    guest_data.close()

    #### split the data and insert into list called: guest
    for i in guest_in:
        guest.append(i.split(","))
        

def perform_calculations():
    global grandtotal
    grandtotal=0
    
    for i in range(len(guest)):
            room_type = str(guest[i][2])
            num_nights = int(guest[i][3])

            if room_type =="SR":
                subtotal = ROOM_RATES[0] * num_nights
#STUDENTS: COMPLETE THESE elif AND else statements
            elif room_type =="DR":
                 subtotal = ROOM_RATES[1] * num_nights
            else:
                 subtotal = ROOM_RATES[2] * num_nights
                
#STUDENTS: COMPLETE THESE CALCULATIONS        
            salestax  = subtotal * TAX_RATES[0]
            occupancy = subtotal * TAX_RATES[1]
            total     = salestax + occupancy + subtotal
             
            grandtotal += total
        
#STUDENTS: ADD THE REST OF THE append statements after this one       
            guest[i].append(subtotal)
            guest[i].append(salestax)
            guest[i].append(occupancy)
            guest[i].append(total)




def open_out_file():        
    global f
    f = open(outfile, 'w')
    f.write('<html> <head> <title> Emerald Beach Hotel & Resort </title>\n')
    f.write('<style> td{text-align: center; padding: 3px} </style> </head>\n')
    f.write('<body style ="background-image: url(wp-hotel.jpg); background-size: cover; margin-top: 3rem; margin-bottom: 3rem; color: rgb(2, 55, 123)">')  #STUDENTS: COMPLETE THIS STATEMENT
    
def create_output_html():
    global f
    
    currency="8,.2f"
    today = str(datetime.datetime.now())
    day_time = today[0:16]

    tr = '<tr><td>'
    td = '</td><td>'
    endtr = '</td></tr>\n'
    colsp = '<tr><td colspan= "8">'

 #STUDENTS: INSERT ALL THE MISSING f.write STATEMENTS HERE

    f.write('\n<table border="7"   style ="background-color: rgba(245, 245, 245, 0.746);  font-family: arial; margin: auto;">\n')   
    f.write( '<tr><td colspan="8" style="padding: 2rem;">' + '\n')
    f.write('<h1>Emerald Beach Hotel & Resort Guest Reprot</h1>' + endtr)
    f.write('<tr><td colspan="8" style="text-align: center; padding: 1rem;">Guest Sales Reprot: ' + day_time + endtr)
    f.write('<tr style="background-color: gray;"><td>Last Name' + td + 'First Name' + td + 'Room Type' + td + 'Num Nights' + td + 'Subtotal' + td + 'Sales Tax' + td + 'Occupancy Tax' + td + 'Total' + endtr)
    for i in range(len(guest)):
         
         f.write(tr + guest[i][0] + td + guest[i][1] + td + guest[i][2] + td + guest[i][3] + td + format(guest[i][4], currency) + td + format(guest[i][5], currency) + td + format(guest[i][6], currency) + td + format(guest[i][7], currency) + endtr)
    f.write(colsp + "Grand Total: " + format(grandtotal, currency) + endtr)

    f.write('</table><br />')
    f.write("</body></html>")
    f.close()
    print('Open ' + outfile + ' to view data.')

##call on main program to execute##
main()
