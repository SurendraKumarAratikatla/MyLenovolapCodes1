from functools import reduce

def add_three(x,y):
    return x+y
li = [1,2,3,4,5]

s = reduce(add_three,li)

print(s)