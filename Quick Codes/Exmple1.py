
l = [1, 2, 8, 3]
#l = [5, 17, 1000, 11]
b = 2
temp = b
ll = []
s = [l[i:j:k] for k in range(1,len(l)) for i in range(len(l)) for j in range(b, len(l)+1) if len(l[i:j:k]) == b and sum(l[i:j:k]) <= 1000]
for i in s:
    if i not in ll:
        ll.append(i)
print(ll)
print(len(ll))
#print(len(set(s)))