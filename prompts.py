from storage import (
    gen_id,
    modify_expenses_storage,
    delete_expense_storage,
    edit_expense_storage,
)
from reports import (
    monthly_total,
)

# Welcome menu for user start
def prompt_start():
    start = input("""
        Welcome to Expense Tracker!\n
        Type the number of the option you would like to pick.\n
        1. ADD AN EXPENSE\n
        2. VIEW MONTHLY EXPENSE REPORT\n
        3. EDIT OR DELETE AN EXISTING EXPENSE\n
        4. EXIT EXPENSE TRACKER\n
    """).strip()

    if start == "1":
        prompt_expense()
    elif start == "2":
        prompt_monthly_total()
    elif start == "3":
        prompt_edit_or_delete_expense()
    elif start == "4":
        return
    else:
        print("Error. Input value not an option.")
        prompt_start()



# Prompt for the user to input an expense
def prompt_expense():
    additions = {}

    def date_get():
        errors = []
        date_str = input("Date (MM-DD-YYYY): ").strip()
        parts = date_str.split("-")
        if len(parts) != 3 or not all(p.isdigit() for p in parts):
            errors.append("date must be in MM-DD-YYYY format")
        else:
            month, day, year = map(int, parts)
            if not (1 <= day <= 31 and 1 <= month <= 12 and 1 <= year <= 9999):
                errors.append("date values are out of range")

            if month == 2 and day > 29:
                errors.append("An invalid day was entered for February. Please try again.")
        if not errors:
            additions["date"] = date_str
        else:
            print("Error. Please fix the following and retry:")
            for err in errors:
                print(f"- {err}")
            date_get()

    def catagory_get():
        errors = []
        category = input("Category: ").strip()
        if not category:
            errors.append("category required")
        if not errors: additions["category"] = category
        else:
            print("Error. Please fix the following and retry:")
            for err in errors:
                print(f"- {err}")
            catagory_get()

    def desc_get():
        errors = []
        description = input("Description: ").strip()
        if not description:
            errors.append("description required")
        if not errors: additions["description"] = description
        else:
            print("Error. Please fix the following and retry:")
            for err in errors:
                print(f"- {err}")
            desc_get()

    def amount_get():
        errors = []
        amount_str = input("Amount (No negative #'s): ").strip()
        try:
            amount = float(amount_str)
            if amount <= 0:
                errors.append("amount must be a positive number")
        except ValueError:
            errors.append("amount must be a number")
        if not errors: additions["amount"] = amount_str
        else:
            print("Error. Please fix the following and retry:")
            for err in errors:
                print(f"- {err}")
            amount_get()

    date_get()
    catagory_get()
    desc_get()
    amount_get()

    additions["id"] = gen_id()
    modify_expenses_storage(additions)

    expense_again = input("Would you like to input another expense? Y/N: ").strip()
    if expense_again.lower() == "y":
        prompt_expense()
    else:
        prompt_start()

# Prompt for the user to view total expenses categorized by month
def prompt_monthly_total():
    year_response = int(input("Which year?: "))
    month_response = int(input("Which month would you like to view? (respond with a number 1 - 12): "))
    
    if 1 <= month_response <= 12:
        total = monthly_total(year_response, month_response)
        print(f"Total for month {month_response}: ${total:.2f}")

        repeat = input("Would you like to view another month? Y/N: ").strip()

        if repeat.lower() == "y":
            prompt_monthly_total()
        else:
            prompt_start()
    else:
        print("- Error. Response was not 1 - 12. Please try again")
        prompt_monthly_total()

# Prompt for the user to edit an expense
def prompt_edit_or_delete_expense():
    # User delete logic
    expense_q_1 = input("Would you like to edit or delete an expense? E/D: ").strip()
    if expense_q_1.lower() == "d":
        prompt_delete()
    # User edit logic
    elif expense_q_1.lower() == "e":
        prompt_edit()

def prompt_delete():
    delete_response = input("Which expense would you like to delete? (respond with the id number): ").strip()
    delete_expense_storage(delete_response)

    delete_repeat = input("Would you like to delete another expense? Y/N: ").strip()
    if delete_repeat.lower() == "y":
        delete_response = input("Which expense would you like to delete? (respond with the id number): ").strip()
        delete_expense_storage(delete_response)
    else:
        prompt_start()

def prompt_edit():
    edit_response = input("Which expense would you like to edit? (respond with the id number): ").strip()
    new_date = input("Date (MM-DD-YYYY): ").strip()
    new_category = input("Category: ").strip()
    new_description = input("Description: ").strip()
    new_amount = input("Amount (No negative #'s): ").strip()
    edit_expense_storage(edit_response, new_date, new_category, new_description, new_amount)

    edit_repeat = input("Would you like to edit another expense? Y/N: ").strip()
    if edit_repeat.lower() == "y":
        prompt_edit()
    else:
        prompt_start()
