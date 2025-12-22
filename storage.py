import os
import csv

storage_file = "data/expenses.csv"
fieldnames = ['id', 'date', 'category', 'description', 'amount']

"""Make sure csv exists to read and write"""
def initialize_expenses_storage():
    os.makedirs("data", exist_ok=True)
    
    if not os.path.exists(storage_file): 
        print("Existing expense data not found. Generating new storage data.")
        with open(storage_file, 'x') as file:
            expenses_header = ",".join(fieldnames) + "\n"
            file.write(expenses_header)

"""Reads csv and returns current listed expenses"""
def read_expenses_storage(filepath):
    with open(filepath, newline='') as csvfile:
        expensereader = csv.DictReader(csvfile)
        read_expenses = []
        for row in expensereader:
            read_expenses.append(row)
        return read_expenses

"""Writes the contents of read_expenses after modification"""
def write_expenses_storage(expenses, filepath):
    with open(filepath, mode='w', newline='') as csvfile:
        expensewriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
        expensewriter.writeheader()
        expensewriter.writerows(expenses)
    print("Data uploaded successfully")
