# Employee.py
import json

class Employee:
    def __init__(self, name: str, age: int, salary: int):
        # Normalize and store employee data
        self.name = name.strip().title()
        self.age = int(age)
        self.salary = int(salary)

        # Validate values
        if self.age < 0:
            raise ValueError("Age cannot be negative")
        if self.salary < 0:
            raise ValueError("Salary cannot be negative")

    def __str__(self):
        # User-friendly display
        return f'{self.name:20} | {self.age:3} | ${self.salary:8}'

    def __repr__(self):
        # Debug-friendly representation
        return f"Employee(name='{self.name}', age={self.age}, salary={self.salary})"

    def to_dict(self):
        """Serialize employee to dict for JSON."""
        return {"name": self.name, "age": self.age, "salary": self.salary}

    @staticmethod
    def from_dict(data):
        """Deserialize employee from dict."""
        return Employee(data['name'], data['age'], data['salary'])

    def __eq__(self, other):
        # Compare employees by name (case-insensitive), age, and salary
        if not isinstance(other, Employee):
            return False
        return (self.name.lower(), self.age, self.salary) == (other.name.lower(), other.age, other.salary)

    def __hash__(self):
        # Enable usage in sets/dicts
        return hash((self.name.lower(), self.age, self.salary))
