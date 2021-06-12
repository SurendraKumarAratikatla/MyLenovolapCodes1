# class prime:
#     def __init__(self,max):
#         self.max = max
#
#     def prime_function(self):
#         count = 0
#         result = []
#         result.append([i for i in range(2,self.max) for j in range(1,i//2) if i%j == 0 and count == 2])
#
#         for i in range(2,self.max):
#             count = 0
#             for j in range(1, i+1):
#                 if i % j == 0:
#                     count +=1
#             #print('{0}: count is {1}'.format(i,count))
#             if count == 2:
#                 result.append(i)
#
#         return result

# obj = prime(20)
# print(obj.prime_function())
# for k in obj.prime_function():
#     print(k)

# p = [x for x in range(2, 20) if all(x % y != 0 for y in range(2, x))]


class prime:
    def __init__(self,max):
        self.max = max

    def prime_function(self):
        count = 0
        result = [x for x in range(2,self.max) if all(x % y != 0 for y in range(2,x))]

        return result

obj = prime(50)
print(obj.prime_function())


s = (y % 2 != 0 for y in range(2,10))
print(s)