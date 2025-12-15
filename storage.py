import os

def ensure_csv():
    if not os.path.exists("data/expenses.csv"): 
        print("Existing expense data not found. Generating new storage data.")
        with open("data/expenses.csv", 'x') as file:
            file.write("id,date,catagory,description,amount")

