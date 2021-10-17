import UserclassObjects
from GetPrice import *
class Theatre:
    def __init__(self,rows,col):
        self.rows=rows
        self.col=col
        self.ticketpurchased=0
        self.ticketpercentage=0
        self.currentincome=0
        self.totalcol=self.rows*col
        self.totalincome =0
        self.users={}
        self.a = [['S' for i in range(self.col)] for j in range(self.rows)]
        if self.totalcol<=60:
            self.totalincome=self.totalcol*10
        else:
            if rows%2:
                self.totalincome=(self.rows//2)*self.col*10 + (self.rows//2)*self.col*8
            else:
                r=self.rows//2
                y=self.rows-r
                self.totalincome=r*self.col*10 + y*self.col*8

    def PrintCinema(self):
        m = 0
        b = 0
        print(end="  ")
        for i in range(1,self.col+1) :
            b = b + 1
            print(b, end=" ")
        print()
        for j in self.a:
            m = m + 1
            print(m, end=" ") 
            print(" ".join(j), sep=",")


    def BuyTicket(self):
        try:
            print('Enter the row-seat number ?')
            print('Enter in (2-5) format, where Row number and Column number are required')
            r,s=input().split('-')
            self.BookSeat(int(r),int(s))
        except:
            print('Please Provide column In The Defined Format.')

    def BookSeat(self,r,s):
        if self.a[r-1][s-1]!='B':
            print('Yeah...!!!Seat Available  Want to Continue ? \n Press "Y" for yes | Press "N" for no')
            res=input()
            if res.lower()=='y':
                price=TicektPrice(r,s,self.totalcol,self.rows)
                print(f'Price for your seat is: {price}$ \n Press "Y" to Continue | Press "N" for Exit')
                resp=input()
                if resp.lower()=='y':
                    name = input("Enter the Name: ")
                    age = input("Enter the Age: ")
                    gender = input("Enter the Gender: ")
                    phone = input("Enter the Phone NO: ")
                    newobj = UserclassObjects.UserInfo()
                    newobj.addDetails(name,age,gender,phone,price)
                    user=newobj.CreateUser((r,s))
                    self.users.update(user)
                    for i in range(len(self.a)) :
                        for j in range(len(self.a[i])):
                            if i==r-1 and j==s-1:
                                self.a[i][j]='B'
                                print(f'Ticket Booked, Your Seat No is {r,s}')
                                self.ticketpurchased=self.ticketpurchased+1
                                self.ticketpercentage=round((self.ticketpurchased/self.totalcol)*100, 2)
                                self.currentincome=self.currentincome+price
                                return
                else:
                    return None
            else:
                return None
        else:
            print('Seat Already Booked. Kindly Choose Another One')

    def BookedTicketUserInfo(self):
        if self.users !={}:
            for i in self.users:
                print('Seat No:',i,'User Details:',self.users[i])
        else:
            print('0 Users Booked Tickets Till Now.')

    def StatisticsMenu(self):
        print('Number of Purchased Tickets:',self.ticketpurchased)
        print('Percentage of Tickets Booked :',self.ticketpercentage,'%')
        print('Current Income:',self.currentincome,'$')
        print('Total Income:',self.totalincome,'$')