from storage import initialize_expenses_storage, read_expenses_storage, write_expenses_storage, storage_file

def prompt_expense():
    date_str = input("Date (DD-MM-YYY): ").strip()
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
        return {
            "date": date_str,
            "category": category,
            "description": description,
            "amount": f"(amount:.2f)",
        }
    
    print("Error. Please fix the following and retry:")
    for err in errors:
        print(f"- {err}")

def main():
    
    initialize_expenses_storage()
    read_expenses_storage(storage_file)

    prompt_expense()
main()

