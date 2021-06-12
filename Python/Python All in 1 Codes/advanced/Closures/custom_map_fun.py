def square(x):
    return x*x

def cube(x):
    return x*x*x

def map_fun(fun, list_values):
    value = []
    for i in list_values:
        value.append(fun(i))
    return value

result = map_fun(square, [1,2,3,4,5])

print(result)