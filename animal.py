# Animal Class

class Animal:

    def __init__(self):
        self.alive = True
        self.spine = True
        self.eyes = True
        self.lungs = True

    def breathe(self):
        print("one breath at a time, in and out")

    def eat(self):
        print("Nom Nom Nom")

    def procreate(self):
        print("time to mate")

    def move(self):
        print("Onwards and upwards")


# breathe is abstracted
cat = Animal()
cat.breathe()



