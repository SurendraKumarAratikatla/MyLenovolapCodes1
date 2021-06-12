import pickle
mylist = ['a', 'b', 'c', 'd']
# with open('datafile.txt', 'wb') as fh:
#    pickle.dump(mylist, fh)

#or

pickle_on = open("datafile2.txt",'wb')
pickle.dump(mylist,pickle_on)

