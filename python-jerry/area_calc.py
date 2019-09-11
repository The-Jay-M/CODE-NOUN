import math
print("Welcome to Area Calculator created by Jerry Mba")
print("1 Triangle\n2 Square\n3 Circle")
shapeNumber= int(input("Please choose a shape from above: "))
if (shapeNumber == 1):
     print("Area of a Triangle")
     breadth= float(input("Enter a breadth: "))
     height= float(input("Enter a height: "))
     area= round((breadth * height / 2), 2)
     print("Area of triangle is", area)
elif (shapeNumber == 2):
     print("Area of a Square")
     length= float(input("Enter a length: "))
     area= round((length * length), 2)
     print("Area of square is", area)
elif (shapeNumber == 3):
     print("Area of a Circle")
     radius= float(input("Enter circle radius: "))
     area= round((math.pi * (radius ** 2)), 2)
     print("Area of circle is", area)
else:
     print("Invalid Selection")
     print("Run the program again and select an option from 1 to 3!")
