# iterator are objects that can we iterated upon, you can built own iterator using iter_and next_methods, collectively called the iterator protocal

my_list = [1,2,3,4,5]

#my_iter = iter(my_list) or

my_iter = my_list.__iter__()

for i in my_list:
    #print(next(my_iter)) or
    print(my_iter.__next__())
