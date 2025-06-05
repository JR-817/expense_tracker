#global_variables
expenses_list = []

def main_menu():
    print("Welcome to the Daily Expense Tracker!\n")
    print("Menu:")
    print("1. Add a new expense")
    print("2. View all expenses")
    print("3. Calculate total and average expense")
    print("4. Clear all expenses")
    print("5. Exit")

def add_expense():          #option 1
    expenses_list.append(float(input()))
    return print("Expense added successfully!")

def view_expense():         #option 2
    if expenses_list:
        print("Your expenses:")
        for i in range(0,len(expenses_list)):
            print(f"{i+1}. {expenses_list[i]}")
    else :
        print("No expenses recorded yet.")
    return

def total_and_average():    #option 3
    if expenses_list:
        print(f"Total expense: {sum(expenses_list)}")
        print(f"Average expense: {(sum(expenses_list)) / (len(expenses_list))}")
    else :
        print("No expenses recorded yet.")
    return
    
def clear_all():            #option 4
    del expenses_list[:] 
    print("All expenses cleared.")
    return

def choose_menu_item():                 
    while True:
        selection = input()
        if selection == "1" :
            add_expense()
        elif selection == "2" :
            view_expense()
        elif selection == "3" :
            total_and_average()
        elif selection == "4" :
            clear_all()
        elif selection == "5" :
            break
    #prints when exiting the program    
    print("Exiting the Daily Expense Tracker. Goodbye!")
            
def main() :
    main_menu()
    choose_menu_item()

main()