# We can create multiple objects for one class,
# Below i am creating two objects(obj1, obj2) for car class

class car:
    car_type = 'TATA'

    def __init__(self, name, mileage):
        self.name = name
        self.mileage = mileage

    def description(self):
        return f" The {self.name} car gives the mileage of {self.mileage}Km/hr and"

    def max_speed(self, speed):
        return f" The {self.name} runs at maximum speed at {speed}Km/hr "

obj1 = car('AUDI', 56.5)

obj2 = car("TOYATO", 66.3)


print(obj1.max_speed(223))
print(obj2.max_speed(250))
