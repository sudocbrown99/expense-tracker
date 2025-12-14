def main():
    try:
        user_welcome_input = int(input(
            "Welcome to Expense Tracker.\n\nPlease choose an option.\n"
            "1. ADD AN EXPENSE\n"
            "2. VIEW MONTHLY EXPENSES\n"
            "3. COMPARE MONTHLY EXPENSES\n"
        ))
        
        if user_welcome_input == 1:
            print("Add Expense")
        else:
            print("Error, option chosen is not available.")
    
    except ValueError:
        print("Error, option chosen is not available.")
main()
