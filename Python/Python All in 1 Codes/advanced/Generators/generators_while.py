def even_generator(max):
    n = 0

    while n < max:
        n += 2
        yield n

even = even_generator(6)

print(next(even))
print(next(even))
