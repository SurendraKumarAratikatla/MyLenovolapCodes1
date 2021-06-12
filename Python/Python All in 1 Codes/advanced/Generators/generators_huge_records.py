import numpy as np

# function, return

# def square_function(numbers):
#     result = []
#     for i in numbers:
#         if i%2 == 0:
#             result.append(i)
#     return result
#
# numbers = np.arange(1,100000)
#
# n = square_function(numbers)
#
# print(n)

# generators, yield

# def square_generators(numbers):
#     for i in numbers:
#         if i%2 == 0:
#             yield i
#
# numbers = np.arange(1,100000)
#
# n = square_generators(numbers)
# for i in n:
#     print(i)


# generators, yield with list comprehension

numbers = np.arange(1,100000)

n = (i for i in numbers if i % 2 ==0)

print(n)

for i in n:
    print(i)

