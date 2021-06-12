import pickle

pickle_in = open("list.pickle", "rb")
s = pickle.load(pickle_in)
print(s)