# By using __ double underscore we can protect our data out the
# scope or out of the class as below


class car:
    def __init__(self, name, mileage):
        self.__name = name
        self._mileage = mileage

    def description(self):
        return f"The {self.__name} car gives the mileage is {self._mileage} Km/Hr"

obj = car('AUDI', 45)

print(obj.description())
print(obj._mileage)
print(obj._car__name) # this gives error because we have protected using double
# underscore to do not access this out of scope or out of class

