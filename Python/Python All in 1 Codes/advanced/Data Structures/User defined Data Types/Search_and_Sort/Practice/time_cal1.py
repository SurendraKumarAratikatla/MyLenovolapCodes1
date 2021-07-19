import time

def find_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + " takes " + str((end-start)*1000) +" mil seconds")
        return result
    return wrapper