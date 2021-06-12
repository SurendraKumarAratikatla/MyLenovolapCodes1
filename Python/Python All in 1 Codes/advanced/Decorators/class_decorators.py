def decorator_function(func):
    def wrapper_function(*args, **kwargs):
        print('wrapper function executed before {}'.format(func.__name__))
        return func(*args, **kwargs)
    return wrapper_function


class decorator_class(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('__call function executed before {}'.format(self.func.__name__))
        return self.func(*args, **kwargs)

@decorator_function
def display():
    print('Display function executed')
display()

@decorator_class
def display_info(name, age):
    print('display info with arguments ({},{})'.format(name, age))
display_info('Chinna',27)