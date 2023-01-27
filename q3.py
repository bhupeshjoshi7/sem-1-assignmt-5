import math
a=float(input("Enter first no.:"))
b=float(input("Enter second no.:"))
c=float(input("Enter third no.:"))
if (a+b>c or b+c>a or c+a>b):
    print("sides are possible")
    s =(a+b+c)/2
    k = ((s)*(s-a)*(s-b)*(s-c))
    area =((k)**0.5)
    print(area,"is the area of triangle")
else:
    print("sides are not possible")