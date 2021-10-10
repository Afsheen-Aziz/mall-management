import mysql.connector as my

passwd = "1234"

def create():
    
    # creating connection and cursor object
    con = my.connect(host="localhost", user="root", password=passwd)
    curs = con.cursor()
    
    # creating database for rock-paper-scissors
    curs.execute("create database if not exists games")

    # creating database, tables and inserting data for the foodcourt
    createtablefun(
        curs,
        "create database if not exists foodcourt",
        "use foodcourt",
        "create table if not exists menu(Sl_No int, Item varchar(50), Price int)",
    )

    menuitems = (
        (1, "CHEESE BURGER", 190),
        (2, "CHICKEN NUGGETS", 150),
        (3, "GREEK PIZZA", 280),
        (4, "SANDWICH", 75),
        (5, "FRENCH FRIES", 100),
        (6, "ICED TEA", 80),
        (7, "KIWI MILKSHAKE", 130),
        (8, "FALOODA", 110),
        (9, "CHICKEN WINGS", 300),
        (10, "MOJITO", 170),
    )
    for menuitem in menuitems:
        curs.execute(
            f"INSERT INTO menu (Sl_No,Item, Price) SELECT * FROM (SELECT {menuitem[0]} AS Sl_No, '{menuitem[1]}' AS Item, {menuitem[2]} as Price) AS temp WHERE NOT EXISTS (SELECT Sl_No FROM menu WHERE Sl_No= {menuitem[0]}) LIMIT 1"
        )
        
   # creating database, tables and inserting data for the theatre
    createtablefun(
        curs,
        "create table if not exists receipt(Sl_No int,Items varchar(50),Price int,Quantity int,Amount int,GST float,Total_Amount float)",
        "create database if not exists theatre",
        "use theatre",
    )

    for seat_no in range(1, 4):
        curs.execute(
            f"create table if not exists screen{seat_no}(Sl_No int, Movies varchar(50),Director varchar(50), Language varchar(50),Time_in_Minutes float)"
        )

    for sc_no in range(1, 4):
        for mov_no in range(1, 4):
            curs.execute(
                f"create table if not exists seat{sc_no}{mov_no}(Seat_No int,Name varchar(50), Price int default 150, Status varchar(20) default 'AVAILABLE') "
            )

    movedetails = (
        (1, 1, "The Conjuring", "James Wan", "English", 112),
        (1, 2, "IT", "Andres Muschietti", "English", 120),
        (1, 3, "The Ring", "Gore Verbinski", "English", 105),
        (2, 1, "The Curse of Lla LLorona", "Michael Chaves", "English", 186),
        (2, 2, "Avengers: The End Game", "Joe Russo", "English", 173),
        (2, 3, "Jurassic World", "Colin Trevorrow", "English", 164),
        (3, 1, "Frozen", "Chris Buck Jennifer Lee", "English", 180),
        (3, 2, "Cinderella", "Kenneth Branagh", "English", 197),
        (3, 3, "Ice Age", "Chris Wedge", "English", 182),
    )
    for movedetail in movedetails:
        curs.execute(
            f"INSERT INTO screen{movedetail[0]}(Sl_No,Movies,Director,Language,Time_in_Minutes) SELECT * FROM (SELECT {movedetail[1]} AS Sl_no, '{movedetail[2]}' AS Movie, '{movedetail[3]}' as Director,'{movedetail[4]}' as Language,{movedetail[5]} as 'Time_in_Minutes')\
                AS temp WHERE NOT EXISTS (SELECT Sl_No FROM screen{movedetail[0]} WHERE Sl_No= {movedetail[1]}) LIMIT 1"
        )

    for sc_no in range(1, 4):  
        for mov_no in range(1, 4):  
            for seat_no in range(1, 11):  
                curs.execute(
                    f"insert into seat{sc_no}{mov_no} (Seat_No) select * from (select '{seat_no}' as Seat_No) as temp where not exists (select Seat_No from seat{sc_no}{mov_no} where Seat_No='{seat_no}') limit 1"
                )
                
    # creating database, tables and inserting data for the parking lot
    createtablefun(
        curs,
        "create database if not exists parkinglot",
        "use parkinglot",
        "create table if not exists login(Name varchar(50),Ph_No bigint,Number_Plate varchar(10),Time varchar(50))",
    )

    curs.execute("create table if not exists ps(Sl_No int,Block varchar(50))")
    curs.execute(
        "create table if not exists pt(Sl_No int,Vehicle_Type varchar(50), Vehicle_Price int)"
    )
    vech_price = 150
    for seat_no in range(1, 5):
        curs.execute(
            f"create table if not exists block{seat_no}(Slot_ID varchar(5),Username varchar(50),Number_Plate varchar(50),Time varchar(50),\
                Status varchar(20) default 'AVAILABLE', Vehicle_Price int default {vech_price})"
        )
        vech_price += 50

    b = [[f"{j}{i}" for i in range(1, 11)] for j in "ABCD"]
    for i in range(1, 5):
        for j in b[i - 1]:
            curs.execute(
                f"insert into block{i} (Slot_ID) select '{j}' as Slot_ID where not exists (select Slot_ID from block{i} where Slot_ID='{j}') limit 1"
            )

    pt = (
        (1, "Two wheelers", 150),
        (2, "Three wheelers", 200),
        (3, "Four wheelers", 250),
        (4, "Multi wheelers", 300),
    )
    ps = (
        (1, "Block 1 for two wheelers"),
        (2, "Block 2 for three wheelers"),
        (3, "Block 3 for four wheelers"),
        (4, "Block 4 for multi wheelers"),
    )
    for data in pt:
        curs.execute(
            f"INSERT INTO pt (Sl_No,Vehicle_Type, Vehicle_Price) SELECT * FROM (SELECT {data[0]} AS Sl_no, '{data[1]}' AS Vehicle_type, {data[2]} as Vehicle_Price) AS temp WHERE NOT EXISTS (SELECT Sl_No FROM pt WHERE Sl_No= {data[0]}) LIMIT 1"
        )
    for data in ps:
        curs.execute(
            f"insert into ps (Sl_No, Block) select * from (select {data[0]} as Sl_No, '{data[1]}' as Block ) as temp where not exists (select Sl_No from ps where Sl_No={data[0]}) limit 1"
        )

    con.commit()
    curs.close()
    con.close()


def createtablefun(curs, arg1, arg2, arg3):
    curs.execute(arg1)
    curs.execute(arg2)
    curs.execute(arg3)