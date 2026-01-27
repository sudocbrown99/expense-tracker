import os
import csv

storage_file = "data/expenses.csv"
fieldnames = ['id', 'date', 'category', 'description', 'amount']

# Make sure csv exists to read and write
def initialize_expenses_storage():
    os.makedirs("data", exist_ok=True)
    
    if not os.path.exists(storage_file): 
        print("Existing expense data not found. Generating new storage data.")
        with open(storage_file, 'x') as file:
            expenses_header = ",".join(fieldnames) + "\n"
            file.write(expenses_header)

# Reads csv and returns current listed expenses
def read_expenses_storage(filepath):
    with open(filepath, newline='') as csvfile:
        expensereader = csv.DictReader(csvfile)
        read_expenses = []
        for row in expensereader:
            read_expenses.append(row)
        return read_expenses

# Generates an id for the row
def gen_id():
    expenses = read_expenses_storage(storage_file)
    if not expenses:
        return 1
    existing_ids = [int(row["id"]) for row in expenses if row.get("id")]
    return max(existing_ids, default=0) + 1

# Actually writes the inputs on the csv
def modify_expenses_storage(additions_dict):
    working_list = read_expenses_storage(storage_file)
    working_list.append(additions_dict)
    write_expenses_storage(working_list, storage_file)

# Writes the contents of read_expenses after modification
def write_expenses_storage(expenses, filepath):
    for index, expense in enumerate(expenses, start=1):
        expense["id"] = index

    with open(filepath, mode='w', newline='') as csvfile:
        expensewriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
        expensewriter.writeheader()
        expensewriter.writerows(expenses)
    print("Data uploaded successfully")

# Deletes a row from the storage csv by ID #
def delete_expense_storage(expense_id):
    expenses = read_expenses_storage(storage_file)
    filtered_expenses = [row for row in expenses if row.get("id") != (expense_id)]

    if len(filtered_expenses) == len(expenses):
        print("No expense found with that ID. Please try again.")
        return

    write_expenses_storage(filtered_expenses, storage_file)

# Edits a row in the storage csv by ID #
def edit_expense_storage(expense_id, new_date, new_category, new_description, new_amount):
    expenses = read_expenses_storage(storage_file)
    expense = [row for row in expenses if row.get("id") == expense_id]
    expense[0]["date"] = new_date
    expense[0]["category"] = new_category
    expense[0]["description"] = new_description
    expense[0]["amount"] = new_amount

    write_expenses_storage(expenses, storage_file)
    print("Expense edited successfully.")