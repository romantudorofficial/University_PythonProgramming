"""
    Animal
"""

class Animal:
    
    def __init__ (self, name, age):
        self.name = name
        self.age = age


    def make_sound (self):
        return "Makes sound."
        

    def animal_info (self):
        return f"Name: {self.name}, Age: {self.age} years"