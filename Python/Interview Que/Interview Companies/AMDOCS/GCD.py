def gcd(a,b):
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a == b:
        return a
    elif a < b:
        while(b):
            a, b = b,a%b
        return a
    else:
        while(a):
            a,b = b,b%a
            return b


# or

# def gcd(a,b):
#     if a == 0:
#         return b
#     elif b == 0:
#         return a
#     elif a == b:
#         return a
#     elif a < b:
#         return gcd(a,b-a)
#     else:
#         return gcd(a-b,b)



print(gcd(48,92))