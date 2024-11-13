"""
    Homework 5 (Laboratory 6)
    Task 3
    Application Starter
"""

from Car import Car
from Motorcycle import Motorcycle
from Truck import Truck



# Car Example

car = Car("Dacia", "Sandero", 2023, 30)
print(car.vehicle_info())
print(car.calculate_mileage(100))
print()



# Motorcycle Example

motorcycle = Motorcycle("Honda", "AA5678", 2008, 50)
print(motorcycle.vehicle_info())
print(motorcycle.calculate_mileage(150))
print()



# Truck Example

truck = Truck("Ford", "Agero", 2024, 16000)
print(truck.vehicle_info())
print(truck.towing_info(1000))