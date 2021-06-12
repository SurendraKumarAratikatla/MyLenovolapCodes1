# def outer_function():
#     a = 5
#     def inner_function():
#        nonlocal a
#        a = 10
#        print('inner function:'+str(a))
#
#     inner_function()
#     print('outer function:'+str(a))
#
# outer_function()



def outer_function(msg):
    def inner_function():
       # nonlocal msg
       # msg = "Hi"
       print('inner function:'+str(msg))
    return inner_function


another = outer_function("Hello")

another()
del outer_function
another()


