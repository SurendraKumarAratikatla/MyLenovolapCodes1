def decorator_function(func):
    def wrapper_function():
        return func()
    return wrapper_function

# def display():
#     print('Display function executed')
# decorator_display = decorator_function(display)
# decorator_display()

#### or

@decorator_function
def display():
    print('Display function executed')
display()