from array import *

a = array('i',[10,20,30,40,50,60])

for x in a:
    print(x)

print(a[0])
print(a[3])

# inserting
a.insert(1,60)
print(a)

# Deletion
a.remove(60)
a.remove(60)
print(a)

# Search
print(a.index(40))

# update
a[2] = 90
print(a)