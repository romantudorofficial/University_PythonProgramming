"""
    Triangle
"""

from Shape import Shape
import math



class Triangle (Shape):
    
    def __init__ (self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
    
    def area (self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))
    
    def perimeter (self):
        return self.side_a + self.side_b + self.side_c