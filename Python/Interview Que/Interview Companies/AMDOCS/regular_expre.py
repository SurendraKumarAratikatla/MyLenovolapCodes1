import re

s = "abcdefghijklmnopqrstuvwxyz"

r = re.split(s, r'(?!p)p')

print(r)

