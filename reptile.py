# showcasing inheritance

from animal import Animal

class Reptile(Animal): # inherit animal class

    def __init__(self):
        super().__init__() # initialising parent/base class - inherit from Animal creating a reptile
        self.cold_blooded = True
        self.tetrapod = None # not all reptiles have 4 legs
        self.hear_chambers = [3, 4]
        self.amniotic_eggs = None  # Not true for all reptiles # none function

    def seek_heat(self):
        print("its chilly outside, i need a sunbed")



    def hunt(self):
        print("Hunting prey")

    def use_venom(self):
        print("if i have it, may as well use it")

    def attract_mate_through_scent(self):
        print("time to put on the aftershave")

bulbasaur = Reptile()

bulbasaur.hunt()
bulbasaur.breathe()







