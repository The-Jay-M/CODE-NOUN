import math

#Display the welcome message
print("Welcome to Area Calculator created by Jerry Mba")

#Display the shape menu
print("1 Triangle\n2 Square\n3 Circle")

#Ask the user to choose a shape
shapeNumber= int(input("Please choose a shape from above: "))

#Use the shape number to determine the shape to have it's area calculated
if (shapeNumber == 1):
     print("Area of a Triangle")
     breadth= int(input("Enter a breadth: "))
     height= int(input("Enter a height: "))
     area= breadth * height / 2
     print("The area of the triangle is", area)
     
elif (shapeNumber == 2):
     print("Area of a Square")
     length= input("Enter the length of the square: ")
     length = int(length)
     area= length * length
     print("The area of the square is", area)
     
elif (shapeNumber == 3):
     print("Area of a Circle")
     radius= int(input("Enter the radius: "))
     area = radius * radius * math.pi
     area= round(area, 2)
     print("The area of the circle is", area)
else:
     print("Invalid Selection")
     print("Run the program again and select an option from 1 to 3!")
