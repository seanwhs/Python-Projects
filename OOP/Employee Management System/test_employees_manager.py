# test_employees_manager.py
import pytest
from Tkinter.Employee_Management.Tkinter.Employee_Management.EmployeesManager import EmployeesManager
from Tkinter.Employee_Management.Tkinter.Employee_Management.Employee import Employee

# --- Fixtures ---
@pytest.fixture
def manager(tmp_path):
    """Create a fresh EmployeesManager with a temporary JSON file."""
    file_path = tmp_path / "test_employees.json"
    return EmployeesManager(file_name=file_path)

# --- Tests ---

def test_add_employee(manager):
    """Test adding a new employee successfully."""
    emp = manager.add_employee("Alice", 30, 5000)
    assert emp.name == "Alice"
    assert emp.age == 30
    assert emp.salary == 5000
    assert emp in manager.employees

def test_add_duplicate_employee(manager):
    """Adding the same employee twice should raise an error."""
    manager.add_employee("Bob", 25, 4000)
    with pytest.raises(ValueError):
        manager.add_employee("Bob", 25, 4500)  # Duplicate by name+age

def test_list_employees(manager):
    """Test listing employees with sorting and filtering."""
    manager.add_employee("Charlie", 28, 3000)
    manager.add_employee("Alice", 30, 5000)
    # Sort by name
    sorted_emps = manager.list_employees(sort_by="name")
    assert sorted_emps[0].name == "Alice"
    # Filter by partial name
    filtered = manager.list_employees(search_term="Cha")
    assert len(filtered) == 1 and filtered[0].name == "Charlie"

def test_delete_employees_with_age(manager):
    """Delete employees in a given age range."""
    manager.add_employee("Dave", 40, 6000)
    manager.add_employee("Eve", 35, 5500)
    deleted = manager.delete_employees_with_age(36, 45)
    # Only Dave should be deleted
    assert len(deleted) == 1 and deleted[0].name == "Dave"
    # Remaining employee is Eve
    assert len(manager.employees) == 1 and manager.employees[0].name == "Eve"

def test_update_salary_by_employee(manager):
    """Update an employee's salary correctly."""
    emp = manager.add_employee("Frank", 29, 4500)
    manager.update_salary_by_employee(emp, 5000)
    assert emp.salary == 5000

def test_remove_employee(manager):
    """Remove a specific employee."""
    emp = manager.add_employee("Grace", 32, 4800)
    manager.remove_employee(emp)
    assert emp not in manager.employees

def test_persistence(manager, tmp_path):
    """Employees should persist to and load from JSON correctly."""
    emp = manager.add_employee("Hank", 31, 5200)
    # Create a new manager pointing to same file
    new_manager = EmployeesManager(file_name=tmp_path / "test_employees.json")
    assert len(new_manager.employees) == 1
    loaded_emp = new_manager.employees[0]
    # Check loaded data matches
    assert loaded_emp.name == "Hank"
    assert loaded_emp.age == 31
    assert loaded_emp.salary == 5200
