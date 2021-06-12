# Without importing the Template class, there are 3 ways to interpolate strings.

name = 'Chris'

# 1. f strings

print(f'Hello {name}')

# 2. % operator

print('Hey %s %s'%(name,name))

# 3. format

print('Hey {0}'.format(name))