from array import *

a = array('i',[1,2,3,4,5,6,7,8,9])

# for i in a:
#     print(i)

# print(a[3])
#
# # insert
# a.insert(1,10)
# print(a)
#
# # update
# a[1] = 11
# print(a)
#
# #search
# print(a.index(11))
#
# #delete
# a.remove(1)
# print(a)


T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]

# for t in T:
#     for i in t:
#         print(i)

print(T[1][2])

#insert
T.insert(2,12)
print(T)

#update
T[0][1] = 10
print(T)

# Delete
del T[2]
print(T)





