# unpacking
a, b = (1,2)
c, _ = (2,3)
print(c)
a,b, *c = (1,2,3,4,5,6,7)
print(a)
print(b)
print(c)
a,b, *_ = (1,2,3,4,5,6,7)

