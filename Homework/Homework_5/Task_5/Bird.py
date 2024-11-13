"""
    Bird
"""

from Animal import Animal



class Bird (Animal):
    
    def __init__ (self, name, age, can_fly = True):
        super().__init__(name, age)
        self.can_fly = can_fly


    def lay_eggs (self):
        return f"{self.name} lays eggs."


    def fly (self):
        if self.can_fly:
            return f"{self.name} is flying!"
        else:
            return f"{self.name} cannot fly."


    def make_sound (self):
        return "Makes beautiful sounds."


    def bird_info (self):
        return f"{self.animal_info()}, Can Fly: {self.can_fly}"