import collections

dict1 = {'day1': 'Mon', 'day2': 'Tue'}
dict2 = {'day3': 'Wed', 'day1': 'Thu'}

res = collections.ChainMap(dict1,dict2)

print(res)
# Creating a single dictionary
print(res.maps)

print("Keys = {}".format(list(res.keys())))
print("Values = {}".format(list(res.values())))


# Print all the elements from the result

for key, value in res.items():
    print("{} = {}".format(key, value))

#Find a specific value in the result

print("day1 in res: {}".format('day1' in res))
print("day4 in res: {}".format('day4' in res))

