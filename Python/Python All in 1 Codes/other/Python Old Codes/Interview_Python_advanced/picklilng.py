import pickle
l = [1,2,3,4]

pickleout = open("list.pickle","wb")
s = pickle.dump(l,pickleout)
pickleout.close()
print(s)

data = [ { 'a':'A', 'b':2, 'c':3.0 } ]
data_string = pickle.dumps(data)
print ('PICKLE:', data_string )

data_obj = pickle.loads(data_string)
print(data_obj)