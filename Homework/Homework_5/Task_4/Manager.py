"""
    Manager
"""

from Employee import Employee



class Manager (Employee):
    
    def __init__ (self, name, salary, team_size):
        super().__init__ (name, "Manager", salary)
        self.team_size = team_size


    def manage_team (self):
        return f"Managing a team of {self.team_size} employees."


    def get_salary (self):
        base_salary = super().get_salary()
        bonus = self.salary * 0.10
        return f"{base_salary} + Bonus: ${bonus:.2f} = Total Salary: ${self.salary + bonus:.2f}"
