# importing modules
import time
import mysql.connector as my
import tabulate

# creating connection and cursor object
con = my.connect(host="localhost", user="root",
                 password="1234", database="parkinglot")
curs = con.cursor(buffered=True)

# declaring variables
log, pt, ps, bl1, bl2, bl3, bl4, name = ("login", "pt", "ps", "block1",
                                         "block2", "block3", "block4", "",)
b1, b2, b3, b4 = [[f"{j}{i}" for i in range(1, 11)] for j in "ABCD"]
sec = time.time()
t = time.ctime(sec)


def display(a):  # fetch and display the table
    curs.execute("select * from {}".format(a))
    rows = curs.fetchall()
    time.sleep(1)
    print(tabulate.tabulate(rows, tablefmt="fancy_grid", headers=curs.column_names))


# display the table with condition ie, display the details corresponding to the number plate while searching
def display_condition(a, b):
    curs.execute("select * from {} where Number_Plate='{}'".format(a, b))
    rows = curs.fetchall()
    c = curs.rowcount
    if c == 0:
        print("Sorry, there is no record of this number plate in the parking lot.\n Please check your number plate again or login to register.")
    else:
        print("Here\'s where you parked your vehicle!")
        time.sleep(1)
        print(tabulate.tabulate(rows, tablefmt="fancy_grid", headers=curs.column_names))


def enter():  # park vehicle

    def login():  # logbook of people who have parked their vehicles
        global name
        name = input("Enter your name: ")
        global numplate
        numplate = input("Enter your number plate: ").upper()
        ph = input("Enter your phone number: ")
        if ph.isdigit():
            curs.execute("insert into login values('{}',{},'{}','{}')".format(
                name, ph, numplate, t))
            con.commit()
            time.sleep(1)
            print("Here's the parking lot table:")
            display(log)
        else:
            print("Please enter a valid phone number")
            login()

        print("---------PARKING BLOCKS---------")
        time.sleep(1)
        display(ps)
        print("---------VEHICLE TYPES IN EACH BLOCK---------")
        time.sleep(1)
        display(pt)
        

    def full_block(b):  # checking if the block is fully booked
        curs.execute("select * from {} where Status='BOOKED'".format(b))
        curs.fetchall()
        count1 = curs.rowcount
        if count1 == 10:
            print("Sorry, this block is fully booked right now. Try again later.")
            return True
        else:
            print("-----Here are the available parking slots-----")


    def choice():  # asking the user to enter vehicle type
        ch = input("Enter the corresponding serial number of your vehicle type: ")
        
        if ch == "1":
            flag = full_block(bl1)
            if flag is not True:
                display(bl1)
                unavail_slot(bl1, b1)
                return bl1
        
        elif ch == "2":
            flag = full_block(bl2)
            if flag is not True:
                display(bl2)
                unavail_slot(bl2, b2)
                return bl2
        
        elif ch == "3":
            flag = full_block(bl3)
            if flag is not True:
                display(bl3)
                unavail_slot(bl3, b3)
                return bl3
        
        elif ch == "4":
            flag = full_block(bl4)
            if flag is not True:
                display(bl4)
                unavail_slot(bl4, b4)
                return bl4
        
        else:
            print("Please enter a valid vehicle type number")
            _ch = choice()
            return _ch


    def unavail_slot(q, w):  # checking if the slot is available
        r = 0
        r = blocks(q, w)
        if r == 1:
            unavail_slot(q, w)


    def blocks(b, n):  # booking the slot
        c = input("Please enter an available slot: ")
        if c.upper() not in n:
            print("Please enter valid input")
            return 1
        else:
            curs.execute("update {} set Status='BOOKED', Username= '{}',Number_Plate='{}', Time='{}' where (Slot_ID = '{}' and Status = 'AVAILABLE') ".format(
                b, name, numplate, t, c))
            con.commit()
            x = curs.rowcount
            if x == 0:
                blocks(b, n)
            else:
                print("------Here's the current block status------")
                display(b)


    def receipt(a):  # printing the receipt
        print("Here's your receipt")
        curs.execute("select A.Slot_Id,A.Username,A.Number_Plate,A.Time,B.Vehicle_Price,B.Vehicle_Type from {} A,pt B where (A.Vehicle_price =B.Vehicle_price and A.Username = '{}') ".format(a, name))
        rows = curs.fetchone()
        time.sleep(1)
        print(tabulate.tabulate(
            [rows], tablefmt="fancy_grid", headers=curs.column_names))

    login()
    rec_ch = choice()
    if rec_ch is not None:
        receipt(rec_ch)
    print(
        """
            Login successful
            Celebrate your day with us!"""
    )


def search():  # searching for the parked vehicle

    nump = input("Enter your number plate: ").upper()
    ch = input("Enter the serial number of your vehicle type: ")
    if ch == "1":
        display_condition(bl1, nump)
    elif ch == "2":
        display_condition(bl2, nump)
    elif ch == "3":
        display_condition(bl3, nump)
        # break
    elif ch == "4":
        display_condition(bl4, nump)
    else:
        print("Please enter a valid vehicle type number")


def logout():  # taking out the parked vehicle and exiting

    bl_num = input(
        "Enter your block in the specified format, for eg: block1: ").lower()
    if bl_num.lower() in ["block1", "block2", "block3", "block4", ]:
        slot_id = input(
            "Enter the Slot ID you parked your vehicle in: ").lower()
        if slot_id.upper() in [*b1, *b2, *b3, *b4]:
            num_plate = input("Enter your number plate: ").upper()
            curs.execute(
                "select * from {} where Number_Plate='{}'".format(bl_num, num_plate))
            if len(curs.fetchall()):
                curs.execute("delete from login where Number_Plate='{}'".format(num_plate))
                curs.execute("update {} set Status='AVAILABLE', Username= NULL ,Number_Plate= NULL, Time= NULL where (Slot_ID = '{}' and Status = 'BOOKED') ".format(bl_num, slot_id))
                con.commit()
                print(
                    """
        
        HOPE YOU ENJOYED YOUR EXPERIENCE AT HEAVENSQUARES!
        We will miss you..
        But we are going to meet again soon..
        GOODBYE !!
                ****************   """
                )
                time.sleep(2)

            else:
                print("Sorry, this number plate is not found.\nPlease check your number plate again or login to register. ")
        else:
            print("Sorry, the Slot ID you entered is incorrect. Please check your Slot ID again or login to register.")
    else:
        print("Sorry, the block you entered is incorrect. Please check your block again and ensure you've entered it in the correct format.")


def start():  # parking lot facilities menu

    global con, curs
    curs.execute("use parkinglot")
    fun = [enter, search, logout]

    while True:
        time.sleep(1)
        user_ch = input(
            """
           *******WELCOME TO HEAVENSQUARES PARKING LOT ******* 
                  Believe in us for the best quality service

            What would you like to do?

            Press 1 to park your vehicle
            Press 2 to search for your parked vehicle
            Press 3 to take out your parked vehicle
            Press 4 to exit from the parking lot 
            
            Please choose your required service: """
        )
        if user_ch.isdigit():
            user_ch = int(user_ch)
            if 0 < user_ch <= len(fun):
                fun[user_ch - 1]()
            elif user_ch == 4:
                break
            else:
                print("Please enter a valid option")
        else:
            print("Please enter an integer")