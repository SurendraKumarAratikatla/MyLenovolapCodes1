from functools import reduce

def add_three(x,y):
    return x+y
li = [1,2,3,4,5]
lli = [1,2,3,4,5]
s = reduce(add_three,li)

print(s)
a = [i for i in map(lambda x,y:x+y,li,lli)]
print(a)
b = map(add_three,li,lli)
#print(list(b))
