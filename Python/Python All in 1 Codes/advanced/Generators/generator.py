def even_generator():
    n = 0
    n += 2
    yield n

    n += 2
    yield n

    n += 2
    yield n

even = even_generator()

print(next(even))

print(next(even))

print(next(even))

