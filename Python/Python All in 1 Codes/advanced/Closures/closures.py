# def outer_fun():
#     msg = 'Hello'
#     def inner_fun():
#         print(msg)
#     return inner_fun
#
# hi_fun = outer_fun()
#
# hi_fun()
# hi_fun()
# hi_fun()


def outer_fun(msg):
    message = msg
    def inner_fun():
        print(msg)
    return inner_fun

hi_fun = outer_fun('HI')
hello_fun = outer_fun('HELLO')

hi_fun()
hello_fun()

