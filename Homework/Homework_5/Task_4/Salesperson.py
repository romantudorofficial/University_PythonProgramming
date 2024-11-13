"""
    Salesperson
"""

from Employee import Employee



class Salesperson(Employee):
    
    def __init__ (self, name, salary, sales_target):
        super().__init__(name, "Salesperson", salary)
        self.sales_target = sales_target


    def make_sale (self):
        return f"Made a sale, aiming to meet a target of {self.sales_target} units."


    def get_salary (self):
        base_salary = super().get_salary()
        commission = self.salary * 0.05
        return f"{base_salary} + Commission: ${commission:.2f} = Total Salary: ${self.salary + commission:.2f}"
