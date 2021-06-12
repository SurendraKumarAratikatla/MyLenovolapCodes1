class employee:
    def __init__(self,name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
e = employee('surendra', 27, 20000)

print("name of employee "+str(e.name))
print("age of employee "+str(e.age))
print("salary of employee "+str(e.salary))

print ("Employee.__doc__:", e.__doc__)
#print ("Employee.__name__:", e.__name__)
print ("Employee.__module__:", e.__module__)
#print ("Employee.__bases__:", e.__bases__)
print ("Employee.__dict__:", e.__dict__ )
