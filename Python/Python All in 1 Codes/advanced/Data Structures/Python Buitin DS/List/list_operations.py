l = [1,2,3,4,5,'hey',9,7,'hello']

# append
l.append(30)
print(l)

# insert
l.insert(0,300)
print(l)

# index
print(l.index(30))

# remove
l.remove(30)
print(l)

#count
print(l.count(30)) # will give repetative elements count

# extend # takes only iterables like list, tuple, dictionaries or sets
l.extend([40,50,60])
print(l)

#reverse
l.reverse()
print(l)

# pop
l.pop()
print(l)

# copy
s = l.copy()
print(s)

# clear
s.clear()
print(s)

# sort
ll = [2,5,3,6,8,6,1,9,7,8,33,4,56,78,66,5,4,3]
ll.sort()
print(ll)

#

print(l.__iter__())
print(l.__dir__())
print(l.__repr__())
