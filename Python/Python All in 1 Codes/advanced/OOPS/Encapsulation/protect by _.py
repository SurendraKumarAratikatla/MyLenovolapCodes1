# By using _ underscore prefix of attribute and method by saying dont use outof scope these, but still we can access these

class car:
    def __init__(self, name, mileage):
        self._name = name # protected variable
        self.mileage = mileage

    def description(self):
        return f"The {self._name} car gives the mileage of {self.mileage} km/hr"

obj = car('AUDI', 34)

print(obj.description())

print(obj._name) # This dont give an error here, because we are saying this shouldn't access
                # out of class cause its protected by underscore, but still we can access


print(obj.mileage)