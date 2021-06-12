l = ['a','b','c','d','e']
index = 0

for i in l:
    print(index,i)
    index += 1

# using enumerate methods gives you index default

for index, value in enumerate(l, start=1):
    print(index, value)
