```python
OOP - object orientated programming. 
•	Viewing your code into an object and manipulating it.
•	Home office has previous applications that have been written using OOP.
•	Must be able to Read and understand OOP.

Class – Setting data or function into the same object for you to capitalize and make a template.
Example:
Class Dog: 
animal_kind = Canine (variable for the class made)
Define method: example bark 
Self.animal_kind 
Return “woof”
# general template ^^

# Instantiation of class – make a dog and use template class.
Fido = Dog()
Print(type(fido))
# bark method 
Print(fido.bark())

OOP – methodology of programming – The Four Pillars 
1.	Encapsulation – process of hiding data and implementation details so the programmer can focus on overall logic. 
2.	Abstraction – don’t always need to know how something works to use it. For example, Driver but not a mechanic how a car works.
3.	Inheritance - inherit that variables and class methods from the parent class.
4.	Polymorphism – methods can have the same name but act differently. 

Abstraction example – class animal 
Class Animal:
Def  __init__(self):       # define initialize self
Define methods: True statements. 
# Define abstract method eg
Def breathe(self):
Print(“ one breath at a time, in and out)

#create animal in class 
Cat = animal() # if cat is animal class then cat will breath and adopt method of def breath 
Cat.breath()

########################################################### showcasing inheritance

from animal import Animal # import animal base class from animal 

class Reptile(Animal): # inherit animal parent class 

    def __init__(self):
        super().__init__() # initialising base class - inherit from Animal creating a reptile
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

bulbasaur.hunt() # self method 
bulbasaur.breathe() # inheratace method 


#################################################################################################################

############################################################### Showcasing Encapsulation

from reptile import Reptile # import class from repltile 

class Snake(Reptile): # create new class as snake 

    def __init__(self): # define self methods 
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
sidney.seek_heat() # Reptile method
sidney.use_tongue_to_smell() # Snake method

# Encapsulation is also really good, for protecting important varibales/objects

# types of modifiers in python

#public - anyone, anywhere can use it
#private - accessible only within the class itself
#protected - accessible within the class and its subclasses

# follow extra steps and revisit video
# _protected
# __private

##################################################################################################################
################################# Polymorphism - last pillar - methods of the same name but act differently 

from snake import Snake

class Python(Snake):
    def __init__(self):
        super().__init__()
        self.large = True
        self.two_lungs = True
        self.venom = False

    def digest_large_prey(self):
        print("ok, hand me the stretchy pants")

    def constrict(self):
        print("and squeeze")

    def climb(self):
        print("up we go")

    def shed_skin(self):
        print("I'm growing out of this now")

    def breathe(self):
        print("I am breathing but I am a Python!")

peter = Python()

peter.breathe() # animal method
peter.eat() # animal method
peter.hunt() # reptile method
peter.use_tongue_to_smell() # snake method


```