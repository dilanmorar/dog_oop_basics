# create dog class
from Animal_class import *

class Dog(Animal):
    def __init__(self, owner, name):
        self.owner = owner
        self.name = name
        self.dog_collar = True
    def eat_bone(self):
        return
    def run(self):
        return
    def greet_owner(self):
        return