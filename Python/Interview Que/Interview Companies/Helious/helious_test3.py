n = int(input("enter your number:"))
p = 0
q = 1
print(p, end=',')
print(q, end=',')

for i in range(0,n-2):
    print(p+q,end=',')
    temp = q
    q = p+q
    p = temp
