def gen_fibonacci(max):
    n1 = 0
    n2 = 1
    for i in (0,max):
        if n1+n2 <= max:
            yield n1
            n1, n2 = n2, n1 + n2

numbers = gen_fibonacci(10)

print(next(numbers))
print(next(numbers))
print(next(numbers))

