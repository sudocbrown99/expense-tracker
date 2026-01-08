from storage import (
    gen_id,
    modify_expenses_storage,
)

def prompt_start():
    start = input("""
        Welcome to Expense Tracker!\n
        Type the number of the option you would like to pick.\n
        1. ADD AN EXPENSE\n
        2. VIEW REPORT\n
    """)
    if start == "1":
        prompt_expense()
    else:
        print("Error. Input value not an option.")
        prompt_start()




def prompt_expense():
    date_str = input("Date (DD-MM-YYYY): ").strip()
    category = input("Category: ").strip()
    description = input("Description: ").strip()
    amount_str = input("Amount (No negative #'s): ").strip()
    
    errors = []

    parts = date_str.split("-")
    if len(parts) != 3 or not all(p.isdigit() for p in parts):
        errors.append("date must be in DD-MM-YYYY format")
    else:
        day, month, year = map(int, parts)
        if not (1 <= day <= 31 and 1 <= month <= 12 and 1 <= year <= 9999):
            errors.append("date values are out of range")

    if not category:
        errors.append("category required")
    
    if not description:
        errors.append("description required")

    try:
        amount = float(amount_str)
        if amount <= 0:
            errors.append("amount must be a positive number")
    except ValueError:
        errors.append("amount must be a number")

    if not errors:
        additions = {
            "id": gen_id(),
            "date": date_str,
            "category": category,
            "description": description,
            "amount": f"{amount:.2f}",
        }
        modify_expenses_storage(additions)
    
    else:
        print("Error. Please fix the following and retry:")
        for err in errors:
            print(f"- {err}")