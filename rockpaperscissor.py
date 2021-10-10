# importing modules
import time
import tabulate
from random import randint
import mysql.connector as my

# creating connection and cursor object
con = my.connect(host="localhost", user="root", password="1234", database="games")
curs = con.cursor(buffered=True)


def display(a):  # fetch and display the table i.e, scoreboard and finalscores
    
    curs.execute("select * from {}".format(a))
    rows = curs.fetchall()
    print(tabulate.tabulate(rows, tablefmt="fancy_grid", headers=curs.column_names))
    time.sleep(1)


def game():  # play the game

    while True:
        curs.execute("create table if not exists scoreboard(Round_no int unique primary key,User_Win char(1),Comp_Win char(1),Draw char(1))")
        c_char1, c_char2, c_char3 = ("Computer has chosen rock","Computer has chosen paper","Computer has chosen scissor",)
        ctr_pwin, ctr_cwin, ctr_draw = 0, 0, 0
        print(
            """ 
        ******* ROCK PAPER SCISSOR - A NEW GENERATION GAME *******
                      Adorn your Life with Games
        
        Hello there, mate!
        You ready to test your luck in this fun game of Rock Paper Scissors? """
        )
        time.sleep(1)
        
        global pname
        pname = input("Enter your name: ")
        print("Good Luck", pname)
        
        t = input("Enter the number of matches you would like to play: ")
        if t.isdigit():
            t = int(t)
            pwin = "Hurrah! " + pname + ". You get a point!"
            cwin = "Oh no... you lose. It's ok. Let's give it one more try! "
            i = 0
            while i <= t:
                if i == t:
                    break
                win = ""
                loss = ""
                draw = ""
                c_choice = randint(1, 3)
                time.sleep(0.4)
                p_choice = input("\n\tPress \n \tr/R for choosing rock \n \tp/P for choosing paper \n \ts/S for choosing scissors \n\nYour choice: ")
                time.sleep(0.3)
                
                if p_choice.lower() == "r":

                    if c_choice == 1:
                        print(c_char1)
                        print("It's a tie")
                        ctr_draw += 1
                        d, w, l = True, False, False

                    elif c_choice == 2:
                        print(c_char2)
                        print(cwin)
                        ctr_cwin += 1
                        l, w, d = True, False, False

                    else:
                        print(c_char3)
                        print(pwin)
                        ctr_pwin += 1
                        w, l, d = True, False, False

                    if d == True:
                        draw = "*"
                    if w == True:
                        win = "*"
                    if l == True:
                        loss = "*"

                    i += 1

                elif p_choice.lower() == "p":

                    if c_choice == 1:
                        print(c_char1)
                        print(pwin)
                        ctr_pwin += 1
                        w, l, d = True, False, False

                    elif c_choice == 2:
                        print(c_char2)
                        print("It's a tie")
                        ctr_draw += 1
                        d, w, l = True, False, False

                    else:
                        print(c_char3)
                        print(cwin)
                        ctr_cwin += 1
                        l, w, d = True, False, False

                    if d == True:
                        draw = "*"
                    if w == True:
                        win = "*"
                    if l == True:
                        loss = "*"

                    i += 1

                elif p_choice.lower() == "s":

                    if c_choice == 1:
                        print(c_char1)
                        print(cwin)
                        ctr_cwin += 1
                        l, d, w = True, False, False

                    elif c_choice == 2:
                        print(c_char2)
                        print(pwin)
                        ctr_pwin += 1
                        w, l, d = True, False, False

                    else:
                        print(c_char3)
                        print("It's a tie")
                        ctr_draw += 1
                        d, w, l = True, False, False

                    if d == True:
                        draw = "*"
                    if w == True:
                        win = "*"
                    if l == True:
                        loss = "*"

                    i += 1

                else:
                    print("Sorry, invalid choice\n")

                curs.execute("insert ignore into scoreboard values('{}','{}','{}','{}')".format(i, win, loss, draw))
                curs.execute("delete from scoreboard where round_no=0")
                con.commit()
                
            print("GAME OVER")
            time.sleep(1)
            print("\n********SCOREBOARD********\n")
            time.sleep(1)
            print("Now, for the results of each round")
            time.sleep(1)
            print("Here's the scoreboard!")
            display("scoreboard")

            curs.execute("create table finalscores(User int,Computer int,Draws int)")
            curs.execute("insert into finalscores values('{}','{}','{}')".format(ctr_pwin, ctr_cwin, ctr_draw))
            con.commit()
            print("\n ****HERE COMES THE FINAL SCORES! **** \n\t HOLD YOUR BREATH.. \n\n")
            time.sleep(2)
            display("finalscores")

            curs.execute("drop table scoreboard")
            curs.execute("drop table finalscores")

            if ctr_pwin > ctr_cwin:
                print("\nCONGRATULATIONS! YOU WIN!")
                print("HEAD OVER TO THE COUNTER TO COLLECT YOUR PRIZE!!")
            elif ctr_pwin < ctr_cwin:
                print("\nSORRY.. The Computer wins.. That's alright. The road to success is always under construction. BETTER LUCK NEXT TIME!")
            else:
                print("\nIT'S A TIE... WELL PLAYED. KEEP IT UP!\n")
            time.sleep(1)
            
            k = input(
                "\nOh! This game seems interesting! How about we play again? \nPress 1 to continue or any other key to exit: ")
            if k != "1":
                print("You're right. Life is not all about games. See ya next time!")
                break
        else:
            print("Please enter an integer")
            
if __name__ =="__main__":
    game()