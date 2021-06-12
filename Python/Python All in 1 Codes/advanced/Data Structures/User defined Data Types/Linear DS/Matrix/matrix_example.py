from numpy import *

a = array([['Mon',18,20,22,17],['Tue',11,18,21,18],
		   ['Wed',15,21,20,19],['Thu',11,20,22,21],
		   ['Fri',18,17,23,22],['Sat',12,22,20,18],
		   ['Sun',13,15,19,16]])

#print(a)
m = reshape(a,(7,5))
#print(m)

#print(m[2])

#print(m[2][4])

# adding a row
m_r = append(m,[['Avg',12,15,13,11]],0) # here 0 is axis position axis is (0,1) = (row, column)
#print(m_r)

# adding column
m_c = insert(m,[4],[[1],[2],[3],[4],[5],[6],[7]],1) # here 1 axis position axis is (0,1) = (row, column)
#print(m_c)

# Delete row
m_d_r = delete(m,2,0)
#print(m_d_r)

# Delete column
m_d_c = delete(m,1,1)
print(m_d_c)

# update row in matrix
m[3] = ['Thu',0,0,0,0]
print(m)
