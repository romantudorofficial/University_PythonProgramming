"""
    Engineer
"""

from Employee import Employee



class Engineer (Employee):
    
    def __init__ (self, name, salary, programming_language):
        super().__init__(name, "Engineer", salary)
        self.programming_language = programming_language


    def code (self):
        return f"Writing code in {self.programming_language}."


    def get_salary (self):
        base_salary = super().get_salary()
        return f"{base_salary} (No bonus for engineers)"
