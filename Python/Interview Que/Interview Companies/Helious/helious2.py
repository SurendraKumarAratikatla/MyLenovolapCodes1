import pandas as pd

def amazon(rows,column,grid):
    clustor_count= 0
    list_last_value_1 = 2 # i am taking this value as 2 because except 0,1
    list_last_value = 2 # i am taking this value as 2 because except 0,1

    # have take loop and taking my each inner list in my grid
    for clustor in grid:
        one_count = 0
        for value in clustor:
            # checking if anyone value value in my list is equal to 1 so making my count as 1
            if value == 1:
                one_count += 1
            list_last_value_1 = value
        # checking if my count value is not equal to 0 then go inside and will count my cluster count
        if one_count != 0:
            clustor_count += 1
            # checking if edjecent rows are having same value i.e. 1 or not if its 1 then go inside
            if list_last_value == 1 and clustor[0] == 1:
                clustor_count -= 1
        list_last_value = list_last_value_1

    print(clustor_count)

amazon(5,4,[[1,1,0,0],[0,0,1,0],[0,0,0,0],[1,0,1,1],[1,1,1,1]])
#amazon(4,4,[[1,1,0,0],[0,0,0,0],[0,0,1,1],[0,0,0,0]])
#amazon(7,7,[[1,0,0,0,0,0,0],[0,1,0,0,0,0,0],[0,0,1,0,0,0,0],[0,0,0,1,0,0,0],[0,0,0,0,1,0,0],[0,0,0,0,0,1,0],[0,0,0,0,0,0,1]])