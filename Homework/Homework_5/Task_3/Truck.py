"""
    Truck
"""

from Vehicle import Vehicle



class Truck (Vehicle):
    
    def __init__ (self, make, model, year, towing_capacity):
        super().__init__(make, model, year)
        self.towing_capacity = towing_capacity


    def towing_info (self, load_weight):
        if load_weight <= self.towing_capacity:
            return f"Load weight: {load_weight}. Within towing capacity."
        else:
            return f"Load weight: {load_weight}. Exceeds towing capacity!"
