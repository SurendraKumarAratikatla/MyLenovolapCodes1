def isvalid_Age(Age):
    Age = 10
    t = str(type(Age))
    if t[8:11] == "int" and Age >= 120:
        return True
    else:
        return False