l = [1,2,3,4]
c = [9,7,8]
l.extend((6,7))
l.extend([9,7,8])


# Function to find HCF the Using Euclidian algorithm
def compute_hcf(x, y):
   while(y):
       x, y = y, x % y
   return x

hcf = compute_hcf(400,3000)
print("The HCF is", hcf)

