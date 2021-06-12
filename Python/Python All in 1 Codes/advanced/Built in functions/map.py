l = [1,2,3,4,5]
ll = [6,7,8,9,10]
#m = [i for i in map(lambda a,b : a+b,l,ll)]
m = [i+j for i,j in zip(l,ll)]

print(m)

add = [i for i in map(lambda a,b: a+b,l,ll)]

print(add)

m = [i+j for i,j in zip(l,ll)]
print(m)