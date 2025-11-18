import json

# Load budget and expenses from a JSON file
def load_budget_data(filepath):
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
            return data['initial_budget'], data['expenses']
    except (FileNotFoundError, json.JSONDecodeError):
        return 0, []  # Return defaults if file is missing or corrupted


# Save current budget and expenses to a JSON file
def save_budget_data(filepath, initial_budget, expenses):
    data = {
        'initial_budget': initial_budget,
        'expenses': expenses
    }
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)


# Add a new expense to the list
def add_expense(expenses, description, amount):
    expenses.append({'description': description, 'amount': amount})
    print(f"Added expense: {description}, Amount: {amount}")


# Calculate the total of all expenses
def get_total_expenses(expenses):
    total = 0
    for expense in expenses:
        total += expense['amount']
    return total


# Calculate remaining budget
def get_balance(budget, expenses):
    return budget - get_total_expenses(expenses)


# Display all budget details
def show_budget_details(budget, expenses):
    print(f'\nTotal Budget: {budget}')
    print('Expenses:')
    if not expenses:
        print('(No expenses yet.)')
    else:
        for expense in expenses:
            print(f" - {expense['description']} :: {expense['amount']}")
    print(f"Total Spent: {get_total_expenses(expenses)}")
    print(f"Remaining Budget: {get_balance(budget, expenses)}")


# Main program loop
def main():
    print("Welcome to Sean's Budget Tracker App")

    filepath = 'budget_data.json'
    initial_budget, expenses = load_budget_data(filepath)

    # Ask for budget if not loaded from file
    if initial_budget == 0:
        initial_budget = float(input('Please enter your initial budget:\n'))

    budget = initial_budget

    while True:
        print('\nWhat would you like to do?')
        print('1. Add an expense')
        print('2. Show budget details')
        print('3. Exit')

        choice = input('Enter your choice (1/2/3): ').strip()

        if choice == '1':
            description = input('Enter expense description: ')
            amount = float(input('Enter expense amount: '))
            add_expense(expenses, description, amount)
        elif choice == '2':
            show_budget_details(budget, expenses)
        elif choice == '3':
            save_budget_data(filepath, initial_budget, expenses)
            print('Budget saved. Exiting Budget App. Goodbye!')
            break
        else:
            print('Invalid choice, please choose again!')


# Run the app
if __name__ == '__main__':
    main()
