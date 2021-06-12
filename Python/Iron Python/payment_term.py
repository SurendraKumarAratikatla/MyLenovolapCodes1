from itertools import tee, islice, chain, izip

def previous_and_next(some_iterable):
    prevs, items, nexts = tee(some_iterable, 3)
    prevs = chain([None], prevs)
    nexts = chain(islice(nexts, 1, None), [None])
    return izip(prevs, items, nexts)

mylist = ['banana', 'orange', 'apple', 'kiwi', 'tomato']

for previous, item, nxt in previous_and_next(mylist):
    print "previous is", previous