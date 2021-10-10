# importing modules
import os
import time
import tabulate
import colorama
colorama.init()

# initializing the counter and game-board
Board = {f"{cell}": f"{cell}" for cell in range(1, 10)}
counter = 0


def resetboard():  # reset the game-board after each game
    
    global Board
    Board = {f"{cell}": f"{cell}" for cell in range(1, 10)}
    global counter
    counter = 0


def win(tn):  # display if the player wins
    
    time.sleep(0.5)
    printBoard()
    print("\nGame Over\n")
    time.sleep(1)
    print(
        " HOORAY!!!" + tn + " YOU WIN! HEAD OVER TO THE COUNTER TO COLLECT YOUR PRIZE!!"
    )
    resetboard()


def printBoard(): # prints the game-board
    
    Board1 = {}
    for cells in Board:
        if Board[cells] == "X":
            Board1[cells] = colorama.Fore.GREEN + "X"
        elif Board[cells] == "O":
            Board1[cells] = colorama.Fore.GREEN + "O"
        else:
            Board1[cells] = colorama.Fore.RED + Board[cells]

    print(
        tabulate.tabulate(
            [
                [Board1[f"{i}"], Board1[f"{i + 1}"], Board1[f"{i + 2}"]]
                for i in range(1, 9, 3)
            ],
            tablefmt="fancy_grid",
        )
    )
    print(colorama.Style.RESET_ALL)


def game():  # play the game
    
    time.sleep(0.5)
    print(
        """
        *******TIC TAC TOE - A  GAME OF STRATEGY*******
                Adding Fun to your Life
                 
        HELLO THERE, MATE!
        READY TO WIN AMAZING PRIZES WITH A FUN GAME OF TIC TAC TOE?!
        CROSS YOUR FINGERS AND HOPE FOR A WIN!
        
        LET'S GET STARTED"""
    )

    input("Press any key to continue")
    
    while True:
        
        global counter
        resetboard()
        tn = "X"
        state = True
        while state:
            
            os.system("cls")
            time.sleep(0.5)
            printBoard()
            
            move = input("It's your turn," + tn + ". Which place do you want to move to?")
            
            if not move.isdigit() or not 1 <= int(move) <= 9:
                print("Please enter a valid position")
                time.sleep(1)
                continue
            
            if Board[move].upper() not in ["X", "O"]:
                Board[move] = tn
                counter += 1
                
            else:
                print("This position is already filled")
                time.sleep(1)
                continue
            
            for i in range(1, 9, 3):
                
                if Board[f"{i}"] == Board[f"{i + 1}"] == Board[f"{i + 2}"]:
                    win(tn)
                    state = False

            for i in range(1, 4):
                
                if (Board[f"{i}"] == Board[f"{i + 3}"] == Board[f"{i + 6}"]): 
                    win(tn)
                    state = False
                    
            if Board["7"] == Board["5"] == Board["3"]:  
                win(tn)
                state = False
                
            elif Board["1"] == Board["5"] == Board["9"]: 
                win(tn)
                state = False

            if counter == 9:
                print("\nGame Over\n")
                time.sleep(0.5)
                printBoard()
                print("AHOY! IT'S A TIE.. WELL PLAYED . KEEP IT UP ! ")
                state = False

            tn = "O" if tn == "X" else "X"
            
        time.sleep(0.5)
        print()
        if input("This game seems interesting, want to play again? \nPress 1 to continue playing or any other key to exit and return to the main menu: ") != "1":
            break


if __name__ == "__main__":
    game()
