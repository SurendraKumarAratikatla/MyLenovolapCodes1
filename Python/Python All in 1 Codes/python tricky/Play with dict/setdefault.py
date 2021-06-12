request =[('data',"1"),('data',"12"),('data',"3"),('data',"4"),('data1',"5"),]
d ={}
for key, value in request:
    d.setdefault(key,[]).append(value)
    print(key)
    print(value)

print(d)


