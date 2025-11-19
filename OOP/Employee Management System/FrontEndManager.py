# FrontEndManager.py
from Tkinter.Employee_Management.Tkinter.Employee_Management.EmployeesManager import EmployeesManager
from utility import input_number

class FrontEndManager:
    def __init__(self, file_name=None):
        # Initialize manager
        self.employees_manager = EmployeesManager(file_name)

    def print_menu(self):
        """Display menu and get user's choice."""
        print("\nProgram options:")
        options = [
            "1) Add a new employee",
            "2) List all employees",
            "3) Delete employees by age range",
            "4) Update salary by name",
            "5) Delete employee by name",
            "6) Exit program"
        ]
        print("\n".join(options))
        return input_number(f"Enter your choice (1-{len(options)}): ", 1, len(options))

    def select_employee_from_list(self, employees):
        """If multiple employees match, let user select one."""
        if not employees:
            return None
        if len(employees) == 1:
            return employees[0]
        print("\nMultiple employees found:")
        for idx, emp in enumerate(employees, 1):
            print(f"{idx}) {emp}")
        choice = input_number(f"Select employee (1-{len(employees)}): ", 1, len(employees))
        return employees[choice - 1]

    def print_employees_table(self, employees):
        """Print employees in table format."""
        if not employees:
            print("\nEmployee list is empty!")
            return
        print("\n{:<20} | {:<3} | {:<10}".format("Name", "Age", "Salary"))
        print("-"*40)
        for emp in employees:
            print(emp)

    def get_partial_name_employee(self, prompt="Enter employee name (partial match allowed): "):
        """Find employee by partial name and let user select if multiple."""
        name = input(prompt).strip()
        employees = self.employees_manager.find_employees_by_name(name, partial_match=True)
        return self.select_employee_from_list(employees)

    def run(self):
        """Main loop of the program."""
        while True:
            choice = self.print_menu()

            if choice == 1:  # Add
                name = input("Enter Employee Name: ").strip()
                age = input_number("Enter Employee Age: ", 0)
                salary = input_number("Enter Employee Salary: ", 0)
                try:
                    emp = self.employees_manager.add_employee(name, age, salary)
                    print(f"Employee {emp.name} added successfully!")
                except ValueError as e:
                    print(f"Error: {e}")

            elif choice == 2:  # List
                sort_by = input("Sort by (name/age/salary, default=name): ").strip().lower() or 'name'
                search_term = input("Filter by name (leave empty for no filter): ").strip() or None
                employees = self.employees_manager.list_employees(sort_by, search_term)
                self.print_employees_table(employees)

            elif choice == 3:  # Delete by age
                age_from = input_number("Enter age from: ", 0)
                age_to = input_number("Enter age to: ", age_from)
                deleted = self.employees_manager.delete_employees_with_age(age_from, age_to)
                if deleted:
                    print(f"Deleted employees: {', '.join(emp.name for emp in deleted)}")
                else:
                    print("No employees found in this age range.")

            elif choice == 4:  # Update salary
                emp = self.get_partial_name_employee()
                if emp:
                    salary = input_number("Enter new salary: ", 0)
                    self.employees_manager.update_salary_by_employee(emp, salary)
                    print(f"Salary of {emp.name} updated to {salary}.")
                else:
                    print("No employee found.")

            elif choice == 5:  # Delete by name
                emp = self.get_partial_name_employee()
                if emp:
                    self.employees_manager.remove_employee(emp)
                    print(f"Employee {emp.name} removed successfully.")
                else:
                    print("No employee found.")

            elif choice == 6:  # Exit
                print("Exiting program. Goodbye!")
                break
