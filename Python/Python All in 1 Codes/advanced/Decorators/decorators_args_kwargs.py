def decorator_function(func):
    def wrapper_function(*args, **kwargs):
        print('wrapper function executed before {}'.format(func.__name__))
        return func(*args, **kwargs)
    return wrapper_function

@decorator_function
def display():
    print('Display function executed')
display()

@decorator_function
def display_info(name, age):
    print('display info with arguments ({},{})'.format(name, age))
display_info('Chinna',27)