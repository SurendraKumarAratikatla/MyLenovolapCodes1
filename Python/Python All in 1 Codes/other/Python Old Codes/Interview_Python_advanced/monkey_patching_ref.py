import monkey_patching

def monkey_f(self):
    print("monkey_f being called...")

print(monkey_patching.myclass.func(self= None))
monkey_patching.myclass.func = monkey_f
obj = monkey_patching.myclass()

print(obj.func())
