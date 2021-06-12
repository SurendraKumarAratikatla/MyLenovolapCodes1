l = [1,2,3,4]

iter_obj = iter(l)

while True:
    try:
        value = next(iter_obj)
        print(value, value, value, value)

    except StopIteration:
        break
