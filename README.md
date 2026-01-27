# Expense Tracker

A simple command-line tool to log, track, and analyze your spending.

## Features

- **Add Expenses**: Log your spending with a date, category, description, and amount.
- **Monthly Reports**: View your total expenses for any specific month and year.
- **Edit/Delete**: Easily modify or remove previous entries using their unique IDs.
- **Data Persistence**: All your data is stored locally in a `data/expenses.csv` file.

## Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/cm-brown/expense-tracker.git
    cd expense-tracker
    ```

2.  **Ensure you have Python installed**:
    This project requires Python 3.x.

## Usage

Run the main script to start the application:

```bash
python3 main.py
```

### Main Menu Options

When you launch the application, you'll be presented with the following options:

1.  **ADD AN EXPENSE**: Enter details for a new expense.
2.  **VIEW MONTHLY EXPENSE REPORT**: See the total amount spent in a specific month.
3.  **EDIT OR DELETE AN EXISTING EXPENSE**: Modify or remove an entry by its ID.
4.  **EXIT EXPENSE TRACKER**: Close the application.

## Data Storage

Your expenses are saved in `data/expenses.csv` with the following fields:
- `id`: A unique identifier for each expense.
- `date`: The date of the expense (MM-DD-YYYY).
- `category`: The category of spending (e.g., Food, Transport).
- `description`: A brief note about the expense.
- `amount`: The cost of the expense.
