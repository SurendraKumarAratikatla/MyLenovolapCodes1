import collections

dict1 = {'day1': 'Mon', 'day2': 'Tue'}
dict2 = {'day3': 'Wed', 'day4': 'Thu'}

res1 = collections.ChainMap(dict1, dict2)
print(res1.maps)

res2 = collections.ChainMap(dict2,dict1)
print(res2.maps)


# Updaing a new value into maps it will update explicitly without calling chainmap again

dict1['DAY5'] = "FRI"

print(res1.maps)