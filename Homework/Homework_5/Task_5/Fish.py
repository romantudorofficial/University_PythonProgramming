"""
    Fish
"""

from Animal import Animal



class Fish (Animal):
    
    def __init__ (self, name, age, has_scales = True):
        super().__init__(name, age)
        self.has_scales = has_scales


    def swim (self):
        return f"{self.name} is swimming."


    def make_sound (self):
        return "Makes little sounds."


    def fish_info (self):
        return f"{self.animal_info()}, Scales: {self.has_scales}"