# Iterators are objects that can be iterated upon.

l = [1,2,3,4,5]

my_list = iter(l)

print(next(my_list))

for i in my_list:
    print(i)