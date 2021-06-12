# Iterators are objects that can be iterated upon, here we will use two iterators methods __iter__() and __next__()

# anything that you can loop over python called iterables, Ex: List is iterable

l = [1,2,3]

iter_obj = l.__iter__()

print(iter_obj)

# for i in iter_obj:
#     print(i)

item1 = iter_obj.__next__()
#item1 = next(iter_obj)
print(item1)

item2 = iter_obj.__next__()
print(item2)

item3 = next(iter_obj)
print(item3)

item4 = next(iter_obj)
print(item4)