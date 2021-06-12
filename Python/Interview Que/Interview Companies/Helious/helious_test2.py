s = input("enter string:")

rev_string = s[::-1]
#print(rev_string)

if s == rev_string:
    print('its a palindrome')
else:
    print("its not a palinrome")