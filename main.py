def main_menu():
    print("Welcome to the Daily Expense Tracker!\n")
    print("Menu:")
    print("1. Add a new expense")
    print("2. View all expenses")
    print("3. Calculate total and average expense")
    print("4. Clear all expenses")
    print("5. Exit")


def only_5():                                        #this is the way that coddy wanted it to loop through the menu
    main_menu()                                      #this is not my prefered way of looping, I prefer make_selection()
    selection = None
    while selection != "5" :
        if selection != "5" :
            selection = input()
        else:  
            break
    print("Exiting the Daily Expense Tracker. Goodbye!")

def make_selection() :                              #User must make a selection from the menu, which loops if the incorrect choice is made
    selection = None                                #in this case, Coddy asked for an infinite loop until the user input is 5
    #print(f"you made selection {selection}")
    while selection != "5" :
        if selection != "5" :
            main_menu()
            selection = input()
        else:  
            break
    print("Exiting the Daily Expense Tracker. Goodbye!")

def main() :
    only_5()

main()