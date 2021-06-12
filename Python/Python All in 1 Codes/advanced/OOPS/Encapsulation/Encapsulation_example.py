class car:
    def __init__(self, name, mileage):
        self._name = name # protected variable
        self.mileage = mileage

    def description(self):
        return f"The {self._name} car gives the mileage of {self.mileage} km/hr"

obj = car('AUDI', 34)

print(obj.description())

print(obj._name)
print(obj.mileage)