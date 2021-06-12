def outer_fun():
    msg = "hello"
    def inner_fun():
        print(msg)
    return inner_fun()

obj = outer_fun()
print(obj)


