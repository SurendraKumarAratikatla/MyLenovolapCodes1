# function with return statement

def square_function(list_of_numbers):
    result = []

    for i in list_of_numbers:
        result.append(i*i)

    return result

squares = square_function([1,2,3,4,5,6,7,8,9])

print(squares)


# generators, yield
def square_generators(list_of_numbers):

    for i in list_of_numbers:
        yield i*i

squares = square_generators([1,2,3,4,5,6,7,8,9])

print(squares)

for i in squares:
    print(i)


# generators, yield with list comprehension

# def square_generators(list_of_numbers):
#     s = (i*i for i in list_of_numbers)
#     yield s
list_of_numbers = [1,2,3,4,5,6]
squares = (i*i for i in list_of_numbers)
#squares = {i*i for i in list_of_numbers}

print(squares)

for ii in squares:
    print(ii)

