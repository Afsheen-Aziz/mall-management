# importing modules
import tabulate
import time

def start():  # run the vending machine
    
    while True:
        coin = input(
            "***** CRAZY BITES VENDING MACHINE ***** \nPlease enter a coin to continue or 0 to exit :"
        )
        if coin == "0":
            break
        columns = [
            [
                "Chocolates",
                "Cool Drinks",
                "Readables",
                "Snacks",
            ]
        ]
        print(tabulate.tabulate(columns, tablefmt="pretty"))

        user_section = int(input("Please enter a section number: "))
        
        if user_section == 1:
            
            try:
                columns = [
                    [
                        "Snickers",
                        "Bounty",
                        "Granola Bar",
                        "Mars",
                        "Pop Tarts",
                        "Skittles",
                    ]
                ]
                print(tabulate.tabulate(columns, tablefmt="pretty"))
                user_choice = input("Please enter your choice: ")
                choices = {
                    "1": "Snickers",
                    "2": "Bounty",
                    "3": "Granola Bars",
                    "4": "Mars",
                    "5": "Pop Tarts",
                    "6": "Skittles",
                }
                print("", f"Hey there! Here is your {choices[user_choice]}!")
                
            except:
                print("No item found")
                
        elif user_section == 2:
            
            try:
                columns = [
                    ["Cola", "Appy Fizz", "Mountain Dew", "Fanta", "Redbull", "Miranda"]
                ]
                print(tabulate.tabulate(columns, tablefmt="pretty"))
                user_choice = input("Please enter your choice: ")
                choices = {
                    "1": "Cola",
                    "2": "Appy Fizz",
                    "3": "Mountain Dew",
                    "4": "Fanta",
                    "5": "Redbull",
                    "6": "Miranda",
                }
                print("", f"Hey! Here is your {choices[user_choice]}!")
                
            except:
                print("No item found")
                
        elif user_section == 3:
            
            try:
                columns = [
                    [
                        "Newspaper",
                        "Balarama",
                        "Twinkle",
                        "Tell me why",
                        "Readers Digest",
                        "Fun Time Magazine",
                    ]
                ]
                print(tabulate.tabulate(columns, tablefmt="pretty"))
                user_choice = input("Please enter your choice: ")
                choices = {
                    "1": "Newspaper",
                    "2": "Balarama",
                    "3": "Twinkle",
                    "4": "Tell me why",
                    "5": "Readers Digest",
                    "6": "Fun Time Magazine",
                }
                print("", f"Hey there! Here is your {choices[user_choice]}!")
                
            except:
                print("No item found")

        elif user_section == 4:
            
            try:
                columns = [
                    ["Kurkure", "Pringles", "Lays", "Cheetos", "Nachos", "Bingo"]
                ]
                print(tabulate.tabulate(columns, tablefmt="pretty"))
                user_choice = input("Please enter your choice: ")
                choices = {
                    "1": "Kurkure",
                    "2": "Pringles",
                    "3": "Lays",
                    "4": "Cheetos",
                    "5": "Nachos",
                    "6": "Bingo",
                }
                print("", f"Hey there! Here is your {choices[user_choice]}!")
                time.sleep(0.5)
                
            except:
                print("No item found")
        else:
            print("Invalid section")
