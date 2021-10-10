# importing modules
import time
import tabulate
import mysql.connector as my

# creating connection and cursor object
con = my.connect(host="localhost", user="root",password="1234", database="theatre")
curs = con.cursor()

choices = ["1", "2", "3", "exit"]

def var():  # fetch and display the table
    time.sleep(0.5)
    rows = curs.fetchall()
    print(tabulate.tabulate(rows, tablefmt="fancy_grid", headers=curs.column_names))


def DigitInput(txt):  # checks if the user input is a number
    while True:
        item_data = input(txt)
        if item_data.isdigit():
            return item_data
        else:
            print("Please enter a number")


def user():  # screen and movie options menu
    while True:
        time.sleep(1)
        print(
            """ 
        ********* WELCOME TO DOLBY THEATRES  *********
            
            Amazing quality services with the highest clarity screens
            Best sound quality ever
            Bringing the world inside
            A theatre you will fall in love with!!

             """
        )
        time.sleep(2)
        print("Here are the screens available and the movies running in each screen")
        time.sleep(1)
        
        for i in range(3):
            print(f"SCREEN{i+1}")
            curs.execute(f"select * from screen{i+1}")
            var()
            time.sleep(0.5)
            
        sc = input("Enter the screen number or type 'exit' to exit the theatre: ").lower()
        
        if sc in ["1", "2", "3"]:
            curs.execute(f"select * from screen{sc}")
            var()
            movchoice = input("Enter the serial number for the corresponding movie name: ")
            if movchoice in ["1", "2", "3"]:
                curs.execute(
                    f"select Seat_No,Price,Status from seat{sc}{movchoice}")
                var()
            else:
                print("Please enter a valid movie number")

        elif sc not in ["1", "2", "3", "exit"]:
            print("Please enter a valid screen number")
            continue

        elif sc == "exit":
            print("THANK YOU FOR VISITING DOLBY THEATRES! Until we meet the next time!")
            break


def options(stno) -> bool:  # theatre facilities menu
    time.sleep(0.5)
    n = input(" What would ypu like to do? \nPress 1 to book \nPress 2 to cancel your ticket \nPress 3 to return to the main menu\nPlease choose your required service:  ")
    
    if n == "1":
        update(stno)
    
    elif n == "3":
        print("Main Menu")
        time.sleep(0.5)
        return False
    
    elif n == "2":
        delete(stno)
    
    else:
        print("Please enter a valid option")
        time.sleep(0.5)
        options(stno)


def update(stno):  # booking tickets
    st = DigitInput("Enter the number of seats you want to book: ")
    st=int(st)
    
    curs.execute("drop table if exists hi")
    curs.execute("create table hi(Seat_No int,Name varchar(50),Price int,Status varchar(50))")

    for _ in range(st):
        while True:
            curs.execute("select Seat_No from seat{} where Status ='BOOKED' ".format(stno))
            BOOKEDSEATS = [int(seat[0]) for seat in curs.fetchall()]
            try:
                s_choice = int(input("Enter the seat number: "))
            except:
                s_choice = 100
            if s_choice not in BOOKEDSEATS and 0 < s_choice < 11:
                name = input("Enter your name: ")
                curs.execute("update seat{} set Name='{}', Status='BOOKED' where Seat_No ={} and Status = 'AVAILABLE'".format(stno, name, s_choice))
                con.commit()
                time.sleep(0.5)
                print(" **** Booking Successful! **** ")
                curs.execute("select * from seat{} where Seat_No={}".format(stno, s_choice))
                var()
                
                curs.execute("insert into hi values({},'{}',150,'BOOKED')".format(s_choice, name))
                con.commit()
                print("Here are the seats for your movie!\n")
                curs.execute("select * from hi")
                var()
                break

            else:
                print("The seat is already booked or is invalid. Please try booking another seat.")
                
    curs.execute("drop table hi")
    time.sleep(1.5)
    print(" YOUR BOOKING IS SUCCESSFUL! THANK YOU AND ENJOY YOUR EXPERIENCE WITH OUR QUALITY SERVICES! ")


def delete(stno):  # cancelling tickets
    while True:
        data = ""
        s_choice = DigitInput("Enter the seat number: ")
        s_choice = int(s_choice)
        
        if 0 < s_choice < 11:
            name = input("Enter your name: ").lower()
            curs.execute("select Name from seat{} where Seat_no={}".format(stno, s_choice))
            w = curs.fetchall()
            data = w[0][0]
            data = data.lower()
            
            if data != '' and data == name:
                curs.execute("update seat{} set Name = NULL,Status='AVAILABLE' where Seat_No={} and Status = 'BOOKED' ".format(stno, s_choice))
                con.commit()
                curs.execute("select * from seat{} ".format(stno))
                var()
                print("Your ticket has been cancelled")
                break
            
            else:
                print("Sorry, your input doesn't match our records")
            
        else:
            print("Please enter a valid seat number")

if __name__ == "__main__":
    user()