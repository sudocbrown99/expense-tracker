from storage import (
    storage_file,
    read_expenses_storage,
)
from datetime import datetime

def monthly_total(user_month):
    amounts = []
    months = []
    
    expense_list = read_expenses_storage(storage_file)
    
    for date in expense_list:
        parsed_date = datetime.strptime(date["date"], "%m-%d-%Y")
        if parsed_date.month == user_month:
            months.append(parsed_date.month)

    for amount in expense_list:
        amounts.append(amount["amount"])

    print(months)

monthly_total(2)