import os
import csv

storage_file = "data/expenses.csv"
total_expenses = []

def initialize_expenses_storage():
    os.makedirs("data", exist_ok=True)
    
    if not os.path.exists(storage_file): 
        print("Existing expense data not found. Generating new storage data.")
        with open(storage_file, 'x') as file:
            file.write("id,date,category,description,amount\n")

def read_expenses_storage(file):
    with open(storage_file, newline='\n') as csvfile:
        expensereader = csv.DictReader(csvfile)
        for row in expensereader:
            print(row)
read_expenses_storage(storage_file)
