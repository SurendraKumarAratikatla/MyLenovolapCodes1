# class fibonacci:
#     def __init__(self,number):
#         self.number = number
#
#     def gen_fibonacci(self):
#         n1 = 0
#         n2 = 1
#         for i in range(0,self.number):
#             #print('i is :'+str(i))
#             #print('n1+ n   2 is:'+ str(n1+n2))
#             if n1 <= self.number:
#                 yield n1
#                 n1, n2 = n2, n1 + n2
#
# f = fibonacci(20)
#
# print(f.gen_fibonacci())
# for i in f.gen_fibonacci():
#     print(i)
#

class f:
    def __init__(self,max):
        self.max = max

    def fibo(self):
        n1 = 0
        n2 = 1
        for i in range(0, self.max):
            if n1 <= self.max:
                yield n1
                n1, n2 = n2, n1 + n2

obj = f(10)
Trace.Write(obj.fibo())

for i in obj.fibo():
    Trace.Write(i)
