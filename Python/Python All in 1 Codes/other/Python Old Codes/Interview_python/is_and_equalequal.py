#What is the difference between “is” and “==”?
#for the record, is checks identity and == checks equality.

a = [1,2,3]
b = a
c = [1,2,3]

if a==b:
    print(True)
else:
    print(False)
if a==c:
    print(True)
else:
    print(False)

if a is b:
    print(True)
else:
    print(False)

if a is c:
    print(True)
else:
    print(False)