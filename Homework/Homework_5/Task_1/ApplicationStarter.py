"""
    Homework 5 (Laboratory 6)
    Task 1
    Application Starter
"""

from Circle import Circle
from Rectangle import Rectangle
from Triangle import Triangle



# Circle Example

circle = Circle(radius = 100)
print("Circle Area:", circle.area())
print("Circle Perimeter:", circle.perimeter(), "\n")



# Rectangle Example

rectangle = Rectangle(width = 4, height = 6)
print("Rectangle Area:", rectangle.area())
print("Rectangle Perimeter:", rectangle.perimeter(), "\n")



# Triangle Example

triangle = Triangle(side_a = 3, side_b = 4, side_c = 5)
print("Triangle Area:", triangle.area())
print("Triangle Perimeter:", triangle.perimeter())