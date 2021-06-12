import json

class A:
    def count(self, st):
        d = {}
        self.st = st
        sss = st.split(' ')
        #count = 0
        for j in sss:
            count = 0
            for k in range(len(sss)):
                if j == sss[k]:
                    count = count+1
    
            d[j] = count
        print(d)

        #print(sss)


        #print(st)

st = "i am surendra surendra"

obj = A()

obj.count(st)

#st = "i am surendra surendra"

#print(st.split(' '))




#d = {"i":1,"am":"1","suremdra":2}