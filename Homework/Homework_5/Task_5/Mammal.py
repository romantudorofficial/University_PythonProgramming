"""
    Mammal
"""

from Animal import Animal



class Mammal (Animal):
    
    def __init__ (self, name, age, has_fur = True):
        super().__init__(name, age)
        self.has_fur = has_fur


    def give_birth (self):
        return f"{self.name} gave birth."


    def make_sound (self):
        return "Makes loud sound."


    def mammal_info (self):
        return f"{self.animal_info()}, Fur: {self.has_fur}"