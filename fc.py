# importing modules
import time
import mysql.connector as my
import tabulate

# creating connection and cursor object
con = my.connect(host="localhost", user="root", password="1234")
curs = con.cursor()
curs.execute("use foodcourt")

# declaring variables
ch = []
reciept = []
recieptno = []
menu = "menu"
receipt = "receipt"
header = ("Sl no", "Items", "Price", "Quantity", "Amount", "GST", "Total_Amount")
 
 
def DigitInput(txt):  # checks if the user input is a number
    
    while True:
        item_data = input(txt)
        if item_data.isdigit():
            return item_data
        else:
            print("Please enter a number")


def display(a):  # to fetch and display the table i.e, receipt and menu
    
    curs.execute("select * from {}".format(a))
    rows = curs.fetchall()
    time.sleep(1)
    print(tabulate.tabulate(rows, tablefmt="fancy_grid", headers=curs.column_names))


def order1():  # place order 
    
    print(" What can we get for you? ")
    display(menu)
    itm_data = DigitInput("Enter the number of items you want to order: ")
    n = int(itm_data)
    if 0 < n < 11:
        order2(n)
    else:
        print("Please enter a valid option")


def order2(n):  # further order details and receipt printing
    
    for i in range(n):
        itm_data = DigitInput("Enter the item number from the above menu: ")
        itm_no = int(itm_data)
        
        curs.execute("select Price from menu where Sl_No={}".format(itm_no))
        r = curs.fetchall()
        if r != []:
            for j in r:  # [(150,)]
                prce = j[0]
                print("The price for the selected item is: ", prce)
                
        curs.execute("select Item from menu where Sl_No={}".format(itm_no))
        r = curs.fetchall()
        if r != []:
            for j in r:  # [(150,)]
                itm = j[0]
                print("The selected item is: ", itm)
                
        qty = input("Enter the quantity: ")
        if qty.isdigit() == False:
            print("Please enter a number for quantity")
        else:
            qty = int(qty)
            total = qty * prce
            gst = (12 / 100) * total
            tpr = total + gst
            reciept.append([itm, prce, qty, total, gst, tpr])
            recieptno.append(i + 1)
            print(tabulate.tabulate(tabular_data=[[recieptno[0], *reciept[len(recieptno) - 1]]],tablefmt="fancy_grid",headers=header,))
            time.sleep(1)
            print(" ORDER PLACED!")
            time.sleep(1)
            
        print(tabulate.tabulate(tabular_data=[[recieptno[i], *reciept[i]] for i in range(len(recieptno))]+ [["", "", "", "", "", "", sum(total[5] for total in (reciept))]],tablefmt="fancy_grid",headers=header,))
        print("""
YOUR ORDER HAS BEEN PLACED SUCCESSFULLY. HEAD OVER TO THE COUNTER WITH THE RECEIPT TO GRAB YOUR BITE.

Note :
To delete an item from your current order, please return to the menu and cancel the required now.
Order cancellation will not be accepted afterwards. Thank You.""")
        
        
def delete():  # cancel order
    
    while True:
        itm_data = DigitInput("Enter the serial number of the item to be cancelled: ")
        itm_no = int(itm_data)
        if len(recieptno) >= itm_no:
            del reciept[recieptno.index(itm_no)]
            del recieptno[len(recieptno) - 1]
            time.sleep(1)
            print(tabulate.tabulate([[recieptno[i], *reciept[i]] for i in range(len(recieptno))]+ [["","","","","","",f"Total: {sum(dat[5] for dat in (reciept))}",]],tablefmt="fancy_grid",headers=header,))
            print("Your item has been cancelled")
            ch = input("Do you want to cancel more items? (y/n): ").lower()
            if ch != "y":
                break
        else:
            print("Sorry, you don't have any more items to cancel")
            break


def enter():  # food court facilities menu
    
    time.sleep(1)
    fun = [order1, delete]
    while True:
        time.sleep(1)
        itm_data = DigitInput(
            """

******* WELCOME TO SNACKOPEDIA *******
  Where food is the star !!

What would you like to do?

Press 1 to order from our collection of mouth watering dishes
Press 2 to delete items from your order
Press 3 to exit the foodcourt and return to the mall menu

Please choose your required service: 
""",
        )
        user_ch = int(itm_data)
        if 0 < user_ch <= len(fun):
            fun[user_ch - 1]()
        elif user_ch == 3:
            print("""
    *** THANK YOU FOR VISITING SNACKOPEDIA. ***
    VISIT US AGAIN WHEN YOUR TUMMY SCREAMS FOR FOOD """)
            break
        else:
            print("Please enter a valid option from the above list ")