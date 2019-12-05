# create animal class

class Animal():
    # define characteristics
    def __init__(self):
        self.alive = True
        self.bones = True
    # define methods
    def eat(self, food):
        return 'nom nom nom ' + food
    def sleep(self):
        return 'zzz'
    def speak(self):
        return 'blah blah blah'

