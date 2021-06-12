import pandas as pd

def amazon(rows,column,grid):
    l = grid
    li = []
    j = 1
    for i in range(1,rows+1):
        #print(i)
        del li[:]
        li.append(l[j:i+1])
        j = j + 1
        #print(li)
        #print(len(li))

df = pd.read_excel('helious_excel.xlsx',index = False)
products_list = df.values.tolist()
print(products_list)
#print(df[1:2])

amazon(5,4,df)