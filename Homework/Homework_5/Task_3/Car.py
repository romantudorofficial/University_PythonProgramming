"""
    Car
"""

from Vehicle import Vehicle



class Car (Vehicle):
    
    def __init__ (self, make, model, year, kilometersPerLiter):
        super().__init__(make, model, year)
        self.kilometersPerLiter = kilometersPerLiter


    def calculate_mileage (self, kilometers):
        fuel_used = kilometers / self.kilometersPerLiter
        return f"Kilometers driven: {kilometers}. Fuel used: {fuel_used:.2f} liters."
