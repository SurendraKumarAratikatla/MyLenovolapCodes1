# def print_msg(msg):
#     def printer():
#         print(msg)
#     printer()
# print_msg('hello')

# or

def print_msg(msg):
# This is the outer enclosing function

    def printer():
# This is the nested function
        print(msg)

    return printer  # this got changed

# Now let's try calling this function.
# Output: Hello
another = print_msg("Hello")
#another()