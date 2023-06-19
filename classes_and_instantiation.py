




# classes - data and function into the same object.

# classes
# creating a class - this is a template

class Dog:# capitalise your class

    animal_kind = "canine" # class variable connected to class above

    def bark(self): # class function = methods
        #print(self.animal_kind) #nothing happening
        self.animal_kind
        return "woof"
# print(Dog.animal_kind)
# print(Dog.bark(Dog))

# instantiation of a class - make a dog

fido = Dog()
lassie = Dog()

print(type(fido)) # its a class inside of file and is a dog <class '__main__.Dog'>
print(type(lassie))
print(fido.animal_kind) # canine
print(lassie.animal_kind)

# bark method
print(fido.bark()) # woof

# class varibales also known as atttibutes can be overwritten
fido.animal_kind = "Big Dog"
print(fido.animal_kind) #
print(lassie.animal_kind)

# be careful of class variables

Dog.animal_kind = "Dolphin"

print(fido.animal_kind) # some might not update
print(lassie.animal_kind)

print(lassie.bark())











