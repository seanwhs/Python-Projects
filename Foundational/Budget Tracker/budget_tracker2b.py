import json
import datetime
import os
import shutil

# Constants
DATA_FILE = 'budget_data.json'
BACKUP_DIR = 'backups'

# Load budget and expenses from a JSON file
def load_budget_data(filepath):
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
            # Ensure expenses have required fields for backward compatibility
            for expense in data.get('expenses', []):
                if 'id' not in expense:
                    expense['id'] = datetime.datetime.now().timestamp()
                if 'date' not in expense:
                    expense['date'] = datetime.datetime.now().isoformat()
                if 'category' not in expense:
                    expense['category'] = 'Uncategorized'
            return data.get('initial_budget', 0), data.get('expenses', [])
    except (FileNotFoundError, json.JSONDecodeError):
        return 0, []  # Return defaults if file is missing or corrupted


# Save current budget and expenses to a JSON file with backup
def save_budget_data(filepath, initial_budget, expenses):
    # Create backup before saving
    create_backup(filepath)
    
    data = {
        'initial_budget': initial_budget,
        'expenses': expenses
    }
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)


# Create a backup of the data file
def create_backup(filepath):
    if not os.path.exists(filepath):
        return
    
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)
    
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_path = os.path.join(BACKUP_DIR, f'budget_backup_{timestamp}.json')
    shutil.copy2(filepath, backup_path)
    print(f"Backup created: {backup_path}")


# Input validation helper
def get_valid_float(prompt, min_value=0):
    while True:
        try:
            value = float(input(prompt))
            if value < min_value:
                print(f"Value must be at least {min_value}.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")


# Add a new expense to the list
def add_expense(expenses, description, amount, category='Uncategorized'):
    expense = {
        'id': datetime.datetime.now().timestamp(),
        'description': description,
        'amount': amount,
        'date': datetime.datetime.now().isoformat(),
        'category': category
    }
    expenses.append(expense)
    print(f"✓ Added: {description} | ${amount:.2f} | {category}")


# Edit an existing expense
def edit_expense(expenses, expense_id):
    for expense in expenses:
        if expense['id'] == expense_id:
            print(f"\nEditing: {expense['description']} | ${expense['amount']:.2f}")
            new_desc = input(f"New description (press Enter to keep '{expense['description']}'): ").strip()
            if new_desc:
                expense['description'] = new_desc
            
            new_amount = input(f"New amount (press Enter to keep ${expense['amount']:.2f}): ").strip()
            if new_amount:
                expense['amount'] = float(new_amount)
            
            new_category = input(f"New category (press Enter to keep '{expense['category']}'): ").strip()
            if new_category:
                expense['category'] = new_category
            
            print("✓ Expense updated!")
            return True
    print("✗ Expense not found.")
    return False


# Delete an expense
def delete_expense(expenses, expense_id):
    for i, expense in enumerate(expenses):
        if expense['id'] == expense_id:
            deleted = expenses.pop(i)
            print(f"✓ Deleted: {deleted['description']} | ${deleted['amount']:.2f}")
            return True
    print("✗ Expense not found.")
    return False


# Calculate the total of all expenses
def get_total_expenses(expenses):
    return sum(expense['amount'] for expense in expenses)


# Calculate remaining budget
def get_balance(budget, expenses):
    return budget - get_total_expenses(expenses)


# Display all budget details in a formatted table
def show_budget_details(budget, expenses):
    print("\n" + "="*60)
    print(f"{'BUDGET SUMMARY':^60}")
    print("="*60)
    print(f"{'Total Budget:':<20} ${budget:.2f}")
    print(f"{'Total Spent:':<20} ${get_total_expenses(expenses):.2f}")
    print(f"{'Remaining:':<20} ${get_balance(budget, expenses):.2f}")
    print("="*60)
    
    if not expenses:
        print("\nNo expenses yet.")
    else:
        print(f"\n{'EXPENSES':^60}")
        print("-"*60)
        print(f"{'ID':<12} {'Date':<12} {'Description':<20} {'Amount':>8} {'Category':<10}")
        print("-"*60)
        
        # Sort expenses by date (newest first)
        sorted_expenses = sorted(expenses, key=lambda x: x['date'], reverse=True)
        
        for expense in sorted_expenses:
            date_str = datetime.datetime.fromisoformat(expense['date']).strftime('%Y-%m-%d')
            print(f"{expense['id']:<12.0f} {date_str:<12} {expense['description']:<20} "
                  f"${expense['amount']:>7.2f} {expense['category']:<10}")
        
        print("-"*60)


# Show monthly summary
def show_monthly_summary(expenses):
    if not expenses:
        print("\nNo expenses to summarize.")
        return
    
    monthly_totals = {}
    for expense in expenses:
        date = datetime.datetime.fromisoformat(expense['date'])
        month_key = date.strftime('%Y-%m')
        monthly_totals[month_key] = monthly_totals.get(month_key, 0) + expense['amount']
    
    print("\n" + "="*40)
    print(f"{'MONTHLY SUMMARY':^40}")
    print("="*40)
    
    for month in sorted(monthly_totals.keys(), reverse=True):
        print(f"{month}: ${monthly_totals[month]:>10.2f}")
    
    print("="*40)


# Search expenses by description
def search_expenses(expenses, keyword):
    results = [e for e in expenses if keyword.lower() in e['description'].lower()]
    
    if not results:
        print(f"\nNo expenses found containing '{keyword}'.")
        return
    
    print(f"\nFound {len(results)} expense(s) containing '{keyword}':")
    for expense in results:
        date_str = datetime.datetime.fromisoformat(expense['date']).strftime('%Y-%m-%d')
        print(f"  - {date_str}: {expense['description']} | ${expense['amount']:.2f}")


# Clear screen helper
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# Main program loop
def main():
    clear_screen()
    print("="*60)
    print("Welcome to Sean's Enhanced Budget Tracker App")
    print("="*60)
    
    initial_budget, expenses = load_budget_data(DATA_FILE)
    
    # Ask for budget if not loaded from file
    if initial_budget == 0:
        initial_budget = get_valid_float('Please enter your initial budget: $')
    
    budget = initial_budget
    
    while True:
        print("\n" + "-"*60)
        print("MAIN MENU")
        print("-"*60)
        print(f"Current Balance: ${get_balance(budget, expenses):.2f}")
        print("-"*60)
        print("1. Add an expense")
        print("2. Show budget details")
        print("3. Edit an expense")
        print("4. Delete an expense")
        print("5. Search expenses")
        print("6. Monthly summary")
        print("7. Change budget")
        print("8. Save & Exit")
        print("-"*60)
        
        choice = input('Enter your choice (1-8): ').strip()
        
        if choice == '1':
            description = input('Enter expense description: ').strip()
            if not description:
                print("✗ Description cannot be empty.")
                continue
            amount = get_valid_float('Enter expense amount: $')
            category = input('Enter category (optional, press Enter for "Uncategorized"): ').strip() or 'Uncategorized'
            add_expense(expenses, description, amount, category)
        elif choice == '2':
            show_budget_details(budget, expenses)
        elif choice == '3':
            show_budget_details(budget, expenses)
            if expenses:
                expense_id = float(input('Enter expense ID to edit: '))
                edit_expense(expenses, expense_id)
        elif choice == '4':
            show_budget_details(budget, expenses)
            if expenses:
                expense_id = float(input('Enter expense ID to delete: '))
                confirm = input('Are you sure? (y/n): ').lower()
                if confirm == 'y':
                    delete_expense(expenses, expense_id)
        elif choice == '5':
            keyword = input('Enter search keyword: ').strip()
            if keyword:
                search_expenses(expenses, keyword)
        elif choice == '6':
            show_monthly_summary(expenses)
        elif choice == '7':
            new_budget = get_valid_float('Enter new budget: $')
            budget = new_budget
            print(f"✓ Budget updated to ${budget:.2f}")
        elif choice == '8':
            save_budget_data(DATA_FILE, initial_budget, expenses)
            print('\n✓ Budget saved successfully!')
            print('Thank you for using Budget Tracker. Goodbye!')
            break
        else:
            print('✗ Invalid choice, please choose again!')


# Run the app
if __name__ == '__main__':
    main()