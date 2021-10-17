from GetPrice import *
import TheatreclassObjects


print('PLEASE MAINTAIN SOCIAL DISTANCING AND WEAR MASK INSIDE THE CINEMA HALL')
print('Please proceed for ticket booking')

rows = int(input("Enter the number of rows:" ))
col = int(input("Enter the number of column:"))
sc=TheatreclassObjects.Theatre(rows,col)
def Menu():
    print('1: Show the Seats')
    print('2: Buy a Ticket')
    print('3: Statistics')
    print('4: Show Booked Ticket User Info')
    print('0: Exit')
    print('*************************')
    print('Please Enter Your Choice ?')
    choice=input()
    if choice=='1':
        sc.PrintCinema()
        Menu()
    elif choice=='2':
        sc.BuyTicket()
        Menu()
    elif choice=='3':
        sc.StatisticsMenu()
        Menu()
    elif choice=='4':
        sc.BookedTicketUserInfo()
        Menu()
    elif choice=='0':
        exit()
    else:
        print('Please Choose From the above Given Options.')
        Menu()

Menu()