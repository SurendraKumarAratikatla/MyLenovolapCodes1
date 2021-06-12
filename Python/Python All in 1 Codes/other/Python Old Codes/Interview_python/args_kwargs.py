def multiply(a,b,*args):
    mul = a*b
    #print(mul)
    #print(args) # args = (3,4,5)

    for num in args:
        mul *= num
    return mul

print(multiply(1, 2, 3, 4, 5))