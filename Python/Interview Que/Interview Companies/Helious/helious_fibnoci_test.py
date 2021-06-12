n = int(input("enter your number:"))
p = 0
q = 1
print(p)
print(q)
l = []
j = 0
for i in range(1,n+1):
    l.append(p)
    l.append(q)
    p = q
    q = p + q
    print(l[j]+l[i])
    j += 1
print(l)



# 0,1,1,2,3,5,8

