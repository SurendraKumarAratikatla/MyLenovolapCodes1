# assigning a function to a variable

def square(x):
    return x*x

f = square(25)

print(square)
print(f)

#############

def square(x):
    return x*x

f = square

print(square)
print(f)
print(f(5))