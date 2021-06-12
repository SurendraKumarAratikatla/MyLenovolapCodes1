import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.copy(old_list)

old_list[1][2] = 'AA'

print("Old list:", old_list)
print("Old list id:", id(old_list[1]))
print("New list:", id(new_list[1]))
print("New list id:", new_list)