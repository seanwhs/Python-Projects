````markdown
# Todo List Manager 📝

A simple command-line Todo List manager built in Python. This program allows you to **create, view, complete, and delete tasks**, with all tasks saved in a JSON file so your list persists between sessions.

---

## Table of Contents
- [Project Overview](#project-overview)
- [How the Code Works](#how-the-code-works)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Functions Overview (Detailed)](#functions-overview-detailed)
- [File Structure](#file-structure)
- [License](#license)

---

## Project Overview

This CLI-based Todo List Manager stores tasks in a `todo_list.json` file.  
It supports the following operations:

- View tasks with their status (pending or completed)
- Add new tasks
- Toggle task completion
- Delete tasks
- Persist tasks across sessions

The program is menu-driven and interacts with the user via the command line. It is simple, easy to use, and demonstrates basic Python programming with file I/O, lists, dictionaries, and functions.

---

## How the Code Works

1. **Loading Tasks:**  
   - At startup, the program tries to load tasks from `todo_list.json`.  
   - If the file is missing or contains invalid JSON, it starts with an empty list.  

2. **Viewing Tasks:**  
   - Displays all tasks in a numbered list with status:
     - ✅ Completed
     - ❌ Pending  
   - If no tasks exist, it prints a friendly message.

3. **Adding a Task:**  
   - Prompts the user to enter a task description.  
   - Creates a new dictionary with `"description"` and `"complete": False`.  
   - Appends it to the task list and saves the list immediately.  

4. **Toggling Task Completion:**  
   - Shows tasks and asks the user to pick one.  
   - Toggles the `"complete"` field of the selected task.  
   - Saves the updated list and confirms the change.

5. **Deleting a Task:**  
   - Shows tasks and asks the user to select one to delete.  
   - Removes the corresponding dictionary from the list.  
   - Saves the updated list and confirms deletion.

6. **Saving Tasks:**  
   - All modifications (add, toggle, delete) are saved to `todo_list.json`.  
   - Ensures tasks persist across program runs.

7. **Main Program Loop:**  
   - Displays a menu repeatedly until the user exits.  
   - Calls appropriate functions based on user input.  
   - Handles invalid input gracefully.

---

## Features

- ✅ View Tasks – See all tasks with their current status.
- ➕ Add Tasks – Add new tasks to your list.
- 🔄 Toggle Completion – Mark tasks as completed or pending.
- ❌ Delete Tasks – Remove tasks permanently.
- 💾 Persistent Storage – All tasks are saved in `todo_list.json`.
- 🖥️ Interactive CLI – Easy-to-use command-line interface.

---

## Installation

1. Ensure **Python 3** is installed:

```bash
python --version
````

2. Clone or download the project:

```bash
git clone https://github.com/yourusername/todo-list-manager.git
cd todo-list-manager
```

3. Run the program:

```bash
python todo.py
```

---

## Usage

1. Launch the program:

```bash
python todo.py
```

2. The main menu will appear:

```
Todo List Manager
1. View Tasks
2. Add Task
3. Toggle Task Completion
4. Delete Task
5. Exit
```

3. Enter the number corresponding to the action you want to perform.
4. Tasks are saved automatically after each change.
5. Exit the program using option 5; your tasks remain saved.

---

## Functions Overview (Detailed)

The program is structured around several key functions. Most of them receive the **task list** as an argument. This list is a Python list of dictionaries. Each dictionary represents a single task with this structure:

```json
{
  "description": "Task text",
  "complete": false
}
```

Passing the list into functions allows them to **read, modify, and save tasks** directly.

---

### 1️⃣ `load_tasks()`

* **Purpose:** Load tasks from the JSON file.
* **Arguments:** None
* **Returns:** A list of task dictionaries.
* **Details:**

  * Attempts to open `todo_list.json`.
  * If the file exists and contains valid JSON, returns the list of tasks.
  * If the file does not exist or is corrupted, returns an empty list.
* **Use Case:** Called at startup to initialize the task list.

---

### 2️⃣ `save_tasks(task_list)`

* **Purpose:** Save the current list of tasks to the JSON file.
* **Arguments:**

  * `task_list` → list of dictionaries representing tasks.
* **Returns:** None
* **Details:**

  * Writes the task list to `todo_list.json` in JSON format.
  * Ensures all changes persist across program runs.
* **Why it receives a dictionary/list:** It needs access to the **current state of tasks** to write them to the file.

---

### 3️⃣ `view_tasks(task_list)`

* **Purpose:** Display all tasks and their completion status.
* **Arguments:**

  * `task_list` → list of task dictionaries.
* **Returns:** None (prints to console)
* **Details:**

  * Loops through each dictionary in `task_list`.
  * Prints an index number, task description, and completion status.
  * Shows a special message if the list is empty.
* **Why it receives a dictionary/list:** To read all tasks and display them dynamically.

---

### 4️⃣ `create_task(task_list)`

* **Purpose:** Add a new task to the list.
* **Arguments:**

  * `task_list` → list of task dictionaries.
* **Returns:** None
* **Details:**

  * Prompts the user for a task description.
  * Creates a new dictionary: `{"description": <text>, "complete": False}`.
  * Appends the dictionary to `task_list`.
  * Calls `save_tasks(task_list)` to persist changes.
* **Why it receives a dictionary/list:** To **append a new task** to the existing list.

---

### 5️⃣ `toggle_complete(task_list)`

* **Purpose:** Change the completion status of a task.
* **Arguments:**

  * `task_list` → list of task dictionaries.
* **Returns:** None
* **Details:**

  * Displays the current tasks using `view_tasks(task_list)`.
  * Prompts the user to select a task by its number.
  * Toggles its `"complete"` value from `True` to `False` or vice versa.
  * Calls `save_tasks(task_list)` to persist changes.
* **Why it receives a dictionary/list:** It needs **direct access to modify the dictionary** representing the selected task.

---

### 6️⃣ `delete_task(task_list)`

* **Purpose:** Remove a task from the list.
* **Arguments:**

  * `task_list` → list of task dictionaries.
* **Returns:** None
* **Details:**

  * Displays the current tasks using `view_tasks(task_list)`.
  * Prompts the user to select a task by its number.
  * Removes the selected dictionary from the list.
  * Calls `save_tasks(task_list)` to update the JSON file.
* **Why it receives a dictionary/list:** To **remove a specific dictionary** from the list.

---

### 7️⃣ `main()`

* **Purpose:** Control the main program loop.
* **Arguments:** None
* **Returns:** None
* **Details:**

  * Calls `load_tasks()` to initialize the task list.
  * Displays a menu repeatedly for user actions.
  * Calls other functions (`view_tasks`, `create_task`, `toggle_complete`, `delete_task`) as needed, passing the **task list dictionary** to them.
  * Loops until the user chooses to exit.
* **Why it doesn't need a task argument:** Because it initializes the task list itself and passes it to all other functions that need it.

---

### Key Takeaways About Passing the Task List

1. **Mutable Object:** The task list is a mutable Python object (list of dictionaries). Any changes inside a function **directly affect the original list** in memory.
2. **Centralized Storage:** All operations (`add`, `toggle`, `delete`) work on the same list.
3. **Persistence:** After every change, the list is saved to JSON to ensure tasks persist across sessions.

---

## File Structure

```
todo.py           # Main Python script
todo_list.json    # JSON file storing tasks (auto-generated)
README.md         # Project documentation
```




