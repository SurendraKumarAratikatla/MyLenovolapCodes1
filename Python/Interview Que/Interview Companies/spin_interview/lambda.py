import functools
l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9, 0]

l3 = [7, 9, 11, 13, 5]
#l =[]
# for i in l1:
#     for j in l2:
#         if l1.index(i) == l2.index(j):
#             l.append(i+j)
#
# print(l)


l = [a+b for a,b in zip(l1,l2)]
print(l)
