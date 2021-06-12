class Person:
    # init method or constructor
    def __init__(self, name,age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        # Sample Method

p = Person('Nikhil',24, 30000)
print('Hello, my name is', p.name)
print('my age is',p.age)
print('and my salary is', p.salary)