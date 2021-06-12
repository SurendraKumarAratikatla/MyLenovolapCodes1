class Audi:
    def description(self):
        return f"This is description function of AUDI car"

class BMW:
    def description(self):
        return f"This is description function of BMW car"

audi = Audi()
bmw = BMW()

for car in (audi, bmw):
    print(car.description())

