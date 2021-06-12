class car:
    car_type = 'TATA'

    def __init__(self, name, mileage):
        self.name = name
        self.mileage = mileage

    def description(self):
        return f" The {self.name} car gives the mileage of {self.mileage}Km/hr and"

    def max_speed(self, speed):
        return f" The {self.name} runs at maximum speed at {speed}Km/hr "

obj = car('AUDI', 56.5)

print(obj.description())
print(obj.max_speed(250))
