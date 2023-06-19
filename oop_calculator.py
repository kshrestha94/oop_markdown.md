# basic calculator using oop method
class Calculator: # creating calculator class
    # defining  self methods
    def __init__(self):
        pass
    def addition(self, x, y): # defining self method for addition
        return x + y

    def subtraction(self, x, y):
        return x - y

    def multiplication(self, x, y):
        return x * y

    def division(self, x, y):
        if y != 0:
            return x / y
        else:
            return "error"


oop_calculator = Calculator() # setting calculator

addition_result = oop_calculator.addition(10, 5)
print("addition:", addition_result)

subtraction_result = oop_calculator.subtraction(10, 5)
print("subtraction:", subtraction_result)

multiplication_result = oop_calculator.multiplication(10, 5)
print("multiplication:", multiplication_result)

division_result = oop_calculator.division(10, 5)
print("subtraction:", division_result)

