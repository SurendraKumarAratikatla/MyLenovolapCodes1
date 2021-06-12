l = 'UUDDLR'
#print(type(l))
j = 0
li = [i for i in l]
#print(li)
#print(type(li))
count = 0
def function():
    global count, j
    for k in li:
        if k == li[j]:
            count = count + 1
            j = j + 1
        else:
            return False
    if count == len(li):
        #print('yes in if')
        return True
    else:
        return False
s = function()
print(s)