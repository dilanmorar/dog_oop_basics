# create animal class

class Animal():
    # define characteristics
    def __init__(self):
        self.alive = True
        self.bones = True
    # define methods
    def eat(self):
        return 'nom nom nom'
    def sleep(self):
        return 'zzz'
    def speak(self):
        return 'noise'

