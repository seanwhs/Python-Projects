# EmployeesManager.py
from Employee import Employee
from operator import attrgetter
import json
from pathlib import Path
import logging

# Logging setup
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

class EmployeesManager:
    DEFAULT_FILE_NAME = "employees.json"

    def __init__(self, file_name=None):
        # Set file and load employees
        self.FILE_NAME = Path(file_name or self.DEFAULT_FILE_NAME)
        self.employees = []
        self.load_employees()

    def add_employee(self, name: str, age: int, salary: int):
        """Add a new employee if not a duplicate."""
        emp = Employee(name, age, salary)
        if any(e.name.lower() == emp.name.lower() and e.age == emp.age for e in self.employees):
            raise ValueError(f"Employee '{emp.name}' with age {emp.age} already exists.")
        self.employees.append(emp)
        self.save_employees()
        return emp

    def list_employees(self, sort_by='name', search_term=None):
        """Return sorted (and optionally filtered) employee list."""
        valid_sort_fields = ['name', 'age', 'salary']
        sort_by = sort_by.lower() if sort_by else 'name'
        if sort_by not in valid_sort_fields:
            sort_by = 'name'

        # Sort employees
        result = sorted(self.employees, key=lambda e: e.name.lower()) if sort_by == 'name' else sorted(self.employees, key=attrgetter(sort_by))

        # Apply search filter if needed
        if search_term:
            search_term_lower = search_term.strip().lower()
            result = [emp for emp in result if search_term_lower in emp.name.lower()]

        return result

    def delete_employees_with_age(self, age_from: int, age_to: int):
        """Delete employees within an age range and return deleted list."""
        deleted = [emp for emp in self.employees if age_from <= emp.age <= age_to]
        self.employees = [emp for emp in self.employees if emp not in deleted]
        self.save_employees()
        return deleted

    def find_employees_by_name(self, name: str, partial_match=False):
        """Find employees by name, optionally allowing partial matches."""
        name_lower = name.strip().lower()
        if partial_match:
            return [emp for emp in self.employees if name_lower in emp.name.lower()]
        return [emp for emp in self.employees if emp.name.lower() == name_lower]

    def update_salary_by_employee(self, emp: Employee, salary: int):
        """Update salary of a given employee."""
        if salary < 0:
            raise ValueError("Salary cannot be negative")
        emp.salary = int(salary)
        self.save_employees()

    def remove_employee(self, emp: Employee):
        """Remove a specific employee."""
        if emp in self.employees:
            self.employees.remove(emp)
            self.save_employees()

    # --- Persistence Methods ---
    def save_employees(self):
        """Save employees to JSON file."""
        try:
            data = [emp.to_dict() for emp in self.employees]
            with self.FILE_NAME.open('w', encoding='utf-8') as f:
                json.dump(data, f, indent=4)
        except Exception as e:
            logging.error(f"Error saving employees: {e}")

    def load_employees(self):
        """Load employees from JSON file, handle errors gracefully."""
        if self.FILE_NAME.exists():
            try:
                with self.FILE_NAME.open('r', encoding='utf-8') as f:
                    data = json.load(f)
                    if isinstance(data, list):
                        self.employees = [Employee.from_dict(emp) for emp in data]
                    else:
                        logging.warning(f"Unexpected JSON format in {self.FILE_NAME}. Starting with empty list.")
                        self.employees = []
            except json.JSONDecodeError:
                logging.warning(f"Failed to decode {self.FILE_NAME}. Starting with empty list.")
                self.employees = []
            except Exception as e:
                logging.warning(f"Unexpected error loading {self.FILE_NAME}: {e}")
                self.employees = []
        else:
            self.employees = []
