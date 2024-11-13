"""
    Homework 5 (Laboratory 6)
    Task 4
    Application Starter
"""

from Manager import Manager
from Engineer import Engineer
from Salesperson import Salesperson



# Manager Example

manager = Manager("Bob", 120000, 10)
print(manager.employee_info())
print(manager.get_salary())
print(manager.manage_team())
print()


# Engineer Example

engineer = Engineer("John", 79000, "Python")
print(engineer.employee_info())
print(engineer.get_salary())
print(engineer.code())
print()



# Salesperson Example

salesperson = Salesperson("Charlie", 50000, 100)
print(salesperson.employee_info())
print(salesperson.get_salary())
print(salesperson.make_sale())