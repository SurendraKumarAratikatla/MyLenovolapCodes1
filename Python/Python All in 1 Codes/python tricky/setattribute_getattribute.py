class Person():
    pass

person = Person()

first_key = "first"
first_value = "Tom"

setattr(person,first_key,first_value)
print(person.first)

first = getattr(person,first_key)
print(first)