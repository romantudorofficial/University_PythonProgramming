"""
    Homework 5 (Laboratory 6)
    Task 2
    Application Starter
"""

from SavingsAccount import SavingsAccount
from CheckingAccount import CheckingAccount



# Checking Account Example

print("Checking Account:")
checking = CheckingAccount("54321", 500)
checking.deposit(1000)
checking.withdraw(500)
print()



# Savings Account Example

print("Savings Account:")
savings = SavingsAccount("12345", 1000)
savings.deposit(1000)
savings.add_interest()
savings.withdraw(500)