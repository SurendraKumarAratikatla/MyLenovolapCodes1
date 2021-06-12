import sys

t = ()
l = []

print(sys.getsizeof(t))
print(sys.getsizeof(l))

t = (1,2)
l = [1,2]

print(sys.getsizeof(t))
print(sys.getsizeof(l))

ll = list(l)
tt = tuple(t)
print(ll)
print(tt)

if ll is not l:
    print(False)

if tt is t:
    print(True)