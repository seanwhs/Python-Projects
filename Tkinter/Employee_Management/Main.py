# Main.py
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from EmployeesManager import EmployeesManager
from Employee import Employee


class EmployeeApp:
    def __init__(self, root, file_name=None):
        self.root = root
        self.root.title("Employee Management System")
        self.manager = EmployeesManager(file_name)
        self.create_widgets()
        self.refresh_employee_list()

    def create_widgets(self):
        # Frame for buttons
        frame_buttons = tk.Frame(self.root)
        frame_buttons.pack(padx=10, pady=5, fill=tk.X)

        tk.Button(frame_buttons, text="Add Employee", command=self.add_employee).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_buttons, text="Update Salary", command=self.update_salary).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_buttons, text="Delete Employee", command=self.delete_employee).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_buttons, text="Delete by Age Range", command=self.delete_by_age_range).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_buttons, text="Refresh List", command=self.refresh_employee_list).pack(side=tk.LEFT, padx=5)

        # Treeview for employee list
        columns = ("Name", "Age", "Salary")
        self.tree = ttk.Treeview(self.root, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)
        self.tree.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

        # Search frame
        frame_search = tk.Frame(self.root)
        frame_search.pack(padx=10, pady=5, fill=tk.X)

        tk.Label(frame_search, text="Search Name:").pack(side=tk.LEFT)
        self.search_var = tk.StringVar()
        tk.Entry(frame_search, textvariable=self.search_var).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_search, text="Search", command=self.search_employee).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_search, text="Clear", command=self.clear_search).pack(side=tk.LEFT, padx=5)

    def refresh_employee_list(self, employees=None):
        for row in self.tree.get_children():
            self.tree.delete(row)
        if employees is None:
            employees = self.manager.list_employees()
        for emp in employees:
            self.tree.insert("", tk.END, values=(emp.name, emp.age, emp.salary))

    def add_employee(self):
        name = simpledialog.askstring("Add Employee", "Enter name:")
        if not name:
            return
        try:
            age = int(simpledialog.askstring("Add Employee", "Enter age:"))
            salary = int(simpledialog.askstring("Add Employee", "Enter salary:"))
            emp = self.manager.add_employee(name, age, salary)
            messagebox.showinfo("Success", f"Employee {emp.name} added!")
            self.refresh_employee_list()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def get_selected_employee(self):
        selected = self.tree.focus()
        if not selected:
            messagebox.showwarning("No selection", "Please select an employee.")
            return None
        values = self.tree.item(selected, "values")
        name, age, salary = values
        matches = self.manager.find_employees_by_name(name)
        if matches:
            return matches[0]
        return None

    def update_salary(self):
        emp = self.get_selected_employee()
        if emp:
            try:
                new_salary = int(simpledialog.askstring("Update Salary", f"Enter new salary for {emp.name}:"))
                self.manager.update_salary_by_employee(emp, new_salary)
                messagebox.showinfo("Success", f"{emp.name}'s salary updated to {new_salary}")
                self.refresh_employee_list()
            except ValueError as e:
                messagebox.showerror("Error", str(e))

    def delete_employee(self):
        emp = self.get_selected_employee()
        if emp:
            confirm = messagebox.askyesno("Confirm Delete", f"Delete {emp.name}?")
            if confirm:
                self.manager.remove_employee(emp)
                messagebox.showinfo("Deleted", f"{emp.name} deleted.")
                self.refresh_employee_list()

    def delete_by_age_range(self):
        try:
            age_from = int(simpledialog.askstring("Delete by Age Range", "Enter age from:"))
            age_to = int(simpledialog.askstring("Delete by Age Range", "Enter age to:"))
            deleted = self.manager.delete_employees_with_age(age_from, age_to)
            messagebox.showinfo("Deleted", f"Deleted {len(deleted)} employee(s).")
            self.refresh_employee_list()
        except ValueError:
            messagebox.showerror("Error", "Invalid age input.")

    def search_employee(self):
        term = self.search_var.get().strip()
        if term:
            employees = self.manager.list_employees(search_term=term)
            self.refresh_employee_list(employees)

    def clear_search(self):
        self.search_var.set("")
        self.refresh_employee_list()


if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeeApp(root)
    root.geometry("500x400")
    root.mainloop()
