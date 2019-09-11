import math
a=float(input("Enter x1: "))
b=float(input("Enter x2: "))
c=float(input("Enter c: "))
d= b**2 - 4 * a * c
if (d>0):
    print("unique roots")
    x1= (-b + math.sqrt(d)) / (2*a)
    x2= (-b - math.sqrt(d)) / (2*a)
    print(x1)
    print(x2)
elif (d==0):
    print("double roots")
    x=b-2*a
    print(x)
else:
    print("complex roots")
        
