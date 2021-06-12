from abc import ABC, abstractmethod

class car(ABC):
    def __init__(self, name):
        self.name = name

    def description(self):
        return f"This is description function of car class"
    @ abstractmethod
    def price(self,x):
        pass

class new(car):
    def price(self,x):
        return f"The {self.name} price is {x} Lacks"

obj = new('TATA')
print(obj.price(20))
print(obj.description())