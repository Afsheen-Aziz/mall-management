import sys
import time
import initial
initial.create()
import fc
import parklot
import rockpaperscissor
import theatre
import tictactoe
import vending_machine

def animate(text):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        if ch != " ":
            time.sleep(0.045)


dial1 = """ 
                       ✨✨✨✨✨✨✨✨✨✨✨✨✨
                     ✨                          ✨
                   ✨   WELCOME TO HEAVENSQUARES   ✨
                      ✨                         ✨
                        ✨✨✨✨✨✨✨✨✨✨✨✨
                        
                          Our mall has it all! """

animate(dial1)
print()
time.sleep(0.5)

dial2 = """
                        It’s all about your needs
                        Enjoy your time with us!

"""
animate(dial2)
time.sleep(0.5)

if input("Do you want to park your vechicle in our safe hands? (y): ").lower() == "y":
    parklot.start()

func = [fc.enter,theatre.user,tictactoe.game,rockpaperscissor.game,
        vending_machine.start,parklot.start,]

while True:
    try:
        time.sleep(0.5)
        ch = int(input(
                """
                        ✨✨✨✨
                 ✨✨✨✨✨✨✨✨✨✨✨
             
              All you need under one roof  
                                    
                 ✨✨✨✨✨✨✨✨✨✨✨
                        ✨✨✨✨

        You have reached the Mall Menu 
        Where would you like to go?

        Press 1 for the Food-Court 
                * We're always in the mood for food!! *

        Press 2 for the Dolby Theatre 
                * Catch films before everyone!!! *

        Press 3 to play TicTacToe 
                * Let the games begin!!! *

        Press 4 to play Rock Paper Scissor 
                * Play for fun!! 
                
        Press 5 for the Vending Machine 
                * Grab a coin, foodies!! *

        Press 6 to return to the Parking-lot 
                * Your vehicle is in safe hands!! *

        Press 7 to Exit
                * It's so hard to see you leave...* \n\t"""
            ))
        
    except:
        ch = 3141
    if 0 < ch <= len(func):
        func[ch - 1]()
        time.sleep(1)
        
    elif ch == 7:
        time.sleep(1)
        print("\n\tIs it really time to say goodbye..?")
        time.sleep(1.5)
        print(
            """
                HOPE YOU ENJOYED YOUR EXPERIENCE AT HEAVENSQUARES!
                We'll meet again soon..
               
                             GOODBYE !!
                     
                        ✨✨✨✨✨✨✨✨✨  """
        )
        time.sleep(2)
        break

    else:
        print("Please enter a valid input from the above list and enjoy your experience discovering the wonders of our mall!")
