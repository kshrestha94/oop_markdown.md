# Showcasing Encapsulation

from reptile import Reptile

class Snake(Reptile):

    def __init__(self):
        super().__init__()
        self.forked_tongue = True
        self.cold_blooded = True
        self.venom = None # not all snakes are venomous
        self.limbs = False
        self.tetrapod = False

    def use_tongue_to_smell(self):
        print("do i say it smells nice, or tastes nice...?")

sidney = Snake()

sidney.breathe() # Animal method
sidney.seek_heat() # Reptile
sidney.use_tongue_to_smell() # Snake method

# Encapsulation is also really good, for protecting important varibales/objects

# types of modifiers in python

#public - anyone, anywhere can use it
#private - accessible only within the class itself
#protected - accessible within the class and its subclasses

# follow extra steps and revisit video
# _protected
# __private

