from abc import ABC, abstractmethod

class abstract_class(ABC):
    def __init__(self, name):
        self.name = name

    @ abstractmethod
    def price(self,x):
        return x

obj = abstract_class('TATA')
print(obj.price(20))