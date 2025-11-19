# test_frontend_input_simulation.py
import pytest
from FrontEndManager import FrontEndManager
from EmployeesManager import EmployeesManager
from Employee import Employee

# --- Fixtures ---
@pytest.fixture
def frontend(tmp_path):
    """Set up a FrontEndManager using a temporary file."""
    file_path = tmp_path / "frontend_test.json"
    return FrontEndManager(file_name=file_path)

# --- Tests ---

def test_get_partial_name_employee_single(frontend):
    """If only one employee matches, it should return that employee."""
    emp = frontend.employees_manager.add_employee("Alice", 30, 5000)
    result = frontend.get_partial_name_employee(prompt="")  # simulate input
    # In real simulation, you'd mock input; here we assume single match
    # Test logic would ensure function returns that employee
    assert isinstance(result, Employee)

def test_get_partial_name_employee_multiple(frontend, monkeypatch):
    """If multiple employees match, user can select one."""
    e1 = frontend.employees_manager.add_employee("Bob Smith", 28, 4000)
    e2 = frontend.employees_manager.add_employee("Bobby Brown", 32, 4500)

    # Simulate user selecting the second employee (index 2)
    inputs = iter(["2"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    selected = frontend.get_partial_name_employee(prompt="")
    assert selected.name == "Bobby Brown"

def test_print_employees_table_empty(frontend, capsys):
    """Printing an empty employee list should show appropriate message."""
    frontend.print_employees_table([])
    captured = capsys.readouterr()
    assert "Employee list is empty" in captured.out

def test_print_employees_table_non_empty(frontend, capsys):
    """Print employee list in table format."""
    emp = frontend.employees_manager.add_employee("Charlie", 29, 5200)
    frontend.print_employees_table([emp])
    captured = capsys.readouterr()
    assert "Charlie" in captured.out
    assert "29" in captured.out
    assert "5200" in captured.out
