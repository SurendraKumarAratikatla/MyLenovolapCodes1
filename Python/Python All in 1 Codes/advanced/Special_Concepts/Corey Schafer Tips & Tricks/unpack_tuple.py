t = (1,2)

print(t)

a, b = (1,2)
print(a)
print(b)

# suppose in above code no longer to use b value but need a value in that case put _ where not needed

a, _ = (3,2)
print(a)

# other test case LHS variables not equal to RHS tuple values

# a, b = (1,2,3,4) # or # a,b,c,d = (1,2) this will not work this cases, we can do it by adding * at last variable

a, b, *c = (1,2,3,4,5,6,7)
# a, b, *_ = (1,2,3,4,5,6,7)

print(a)
print(b)
print(c)

# other text case

a, b, *c, d = (1,2,3,4,5,6,7,8,9,10)
print(a)
print(b)
print(c)
print(d)


