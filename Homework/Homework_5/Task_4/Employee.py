"""
    Employee
"""

class Employee:
    
    def __init__ (self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary


    def get_salary (self):
        return f"Salary: ${self.salary}"


    def employee_info (self):
        return f"Name: {self.name}, Position: {self.position}"
