# create dog class
from Animal_class import *

class Dog(Animal):
    def __init__(self, owner, name, colour = 'no colour'):
        self.owner = owner
        self.name = name
        self.dog_collar = colour
    def eat_bone(self):
        return 'eats bone'
    def run(self):
        return 'runs'
    def greet_owner(self):
        return 'licks owner'
    def speak(self):
        return 'woof woof'