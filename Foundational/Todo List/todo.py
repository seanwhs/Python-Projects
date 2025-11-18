import json

FILE_NAME = 'todo_list.json'

# 📝 Plan of Action:
# 1️⃣ Load tasks from JSON file (or start empty)
# 2️⃣ Display tasks with status
# 3️⃣ Add new tasks
# 4️⃣ Toggle task completion
# 5️⃣ Delete tasks
# 6️⃣ Save tasks after any change
# 7️⃣ Loop until user exits

# 📂 Load tasks from JSON or return empty list
def load_tasks():
    """Load tasks from a JSON file, or return an empty list if not found or invalid."""
    try:
        with open(FILE_NAME, 'r') as file:
            return json.load(file)  # ✅ Return task list
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# 💾 Save tasks to JSON
def save_tasks(task_list):
    """Save the task list to the JSON file."""
    try:
        with open(FILE_NAME, 'w') as file:
            json.dump(task_list, file, indent=4)
    except Exception as e:
        print('Failed to save:', e)

# 📋 Display all tasks
def view_tasks(task_list):
    """Display all tasks with their completion status."""
    if not task_list:
        print('\nNo tasks to display.')
    else:
        print('\nTodo List:')
        for index, task in enumerate(task_list):
            status = "[✅ Completed]" if task['complete'] else "[❌ Pending]"
            print(f'{index + 1}. {task["description"]} {status}')

# ➕ Add a new task
def create_task(task_list):
    """Add a new task."""
    description = input('\nEnter task description:\n').strip()
    if description:
        task_list.append({"description": description, "complete": False})
        save_tasks(task_list)
        print('Task added successfully!')
    else:
        print('Description cannot be empty.')

# ✅ Toggle task completion
def toggle_complete(task_list):
    """Mark a specific task as completed."""
    view_tasks(task_list)
    if not task_list:
        return
    
    try:
        task_number = int(input('\nEnter task number to toggle completion: ').strip())
        if 1 <= task_number <= len(task_list):
            task = task_list[task_number - 1]
            task['complete'] = not task['complete']  # Toggle status
            save_tasks(task_list)
            status_text = "complete" if task['complete'] else "pending"
            print(f"Task '{task['description']}' marked as {status_text}.")
        else:
            print('Invalid task number.')
    except ValueError:
        print('Enter a valid number.')

# ❌ Delete a task
def delete_task(task_list):
    """Delete a task from the todo list."""
    view_tasks(task_list)
    if not task_list:
        return

    try:
        task_number = int(input('\nEnter task number to delete: ').strip())
        if 1 <= task_number <= len(task_list):
            deleted_task = task_list.pop(task_number - 1)
            save_tasks(task_list)
            print(f"Deleted task: '{deleted_task['description']}'")
        else:
            print('Invalid task number.')
    except ValueError:
        print('Enter a valid number.')

# 🔄 Main program loop
def main():
    """Main program loop."""
    task_list = load_tasks()

    while True:
        print('\nTodo List Manager')
        print('1. View Tasks')
        print('2. Add Task')
        print('3. Toggle Task Completion')
        print('4. Delete Task')
        print('5. Exit')

        choice = input('Enter your choice: ').strip()
        
        if choice == '1':
            view_tasks(task_list)
        elif choice == '2':
            create_task(task_list)
        elif choice == '3':
            toggle_complete(task_list)
        elif choice == '4':
            delete_task(task_list)
        elif choice == '5':
            print('Goodbye 👋')
            break
        else:
            print('Invalid choice. Please try again.')

# ▶️ Run the app
if __name__ == "__main__":
    main()
