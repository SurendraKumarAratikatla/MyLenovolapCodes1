from functools import reduce

# num1 = 100000000
# num2 = 10000000000

# or

num1 = 100_000_000
num2 = 10_000_000_000

sum = lambda x,y:x+y
print(sum(num1,num2))

# f string use for separate at result
print(f'{sum(num1,num2):,}')