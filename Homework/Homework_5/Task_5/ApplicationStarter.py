"""
    Homework 5 (Laboratory 6)
    Task 5
    Application Starter
"""

from Mammal import Mammal
from Bird import Bird
from Fish import Fish



# Mammal Example

mammal = Mammal("Lion", 13)
print(mammal.mammal_info())
print(mammal.make_sound())
print(mammal.give_birth())
print()


# Bird Example

bird = Bird("Eagle", 2)
print(bird.bird_info())
print(bird.make_sound())
print(bird.fly())
print()



# Fish Example

fish = Fish("Goldfish", 1)
print(fish.fish_info())
print(fish.make_sound())
print(fish.swim())