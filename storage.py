import os
import csv

storage_file = "data/expenses.csv"
total_expenses = [{'id': '1', 'date': 'ad', 'category': 'ac', 'description': 'aD', 'amount': 'aa'}, {'id': '2', 'date': 'bd', 'category': 'bc', 'description': 'bD', 'amount': 'ba'}, {'id': '3', 'date': 'cd', 'category': 'cc', 'description': 'cD', 'amount': 'ca'}]
fieldnames = ['id', 'date', 'category', 'description', 'amount']

def initialize_expenses_storage():
    os.makedirs("data", exist_ok=True)
    
    if not os.path.exists(storage_file): 
        print("Existing expense data not found. Generating new storage data.")
        with open(storage_file, 'x') as file:
            file.write("id,date,category,description,amount\n")

def read_expenses_storage(file):
    with open(storage_file, newline='') as csvfile:
        expensereader = csv.DictReader(csvfile)
        for row in expensereader:
            total_expenses.append(row)
        print(total_expenses)

def write_expenses_storage(list, file):
    with open(storage_file, mode='w', newline='') as csvfile:
        expensewriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
        expensewriter.writeheader()
        expensewriter.writerows(total_expenses)
    print("Data uploaded successfully")
