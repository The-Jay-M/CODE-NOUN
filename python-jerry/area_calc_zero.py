#PROPERLY COMMENT OUT THIS CODE LATER

import math
while True:
    print("Welcome to Area Calculator.")
    def circle():
        #cirlce is pi*r^2
        r = float(input(">>>Enter r\n>>> "))
        r = round(math.pi * r ** 2, 2)
        return print(">>>AREA is {}cm squared".format(r))
    def square():
        #square is l x l
        l = float(input(">>>Enter l\n>>> "))
        l =  l *l
        return print(">>>AREA is {}cm squared".format(l))
    def triangle():
        #triangle is 0.5b x h
        b = float(input(">>>Enter b\n>>> "))
        h = float(input(">>>Enter h\n>>> "))
        a = round(0.5 * b * h, 2)
        return print(">>>AREA is {}cm squared".format(a))
    print(">>>Shapes Available")
    print(">>>C - Circle\n>>>S - Square\n>>>T - Triangle")

    
    def command():
        
        shape = input(">>>Type in a shape or it's letter: ").capitalize()
        if shape == "C" or shape == "Circle":
            circle()
        elif shape == "S" or shape == "Square":
            square()
        elif shape == "T" or shape == "Triangle":
            triangle()
        else:
            print(">>>Invalid Input, please retry")

            
    command()
    pass
    print("Are you done?\n>>>Yes \ No")
    ask = input("*** ").capitalize()
    if ask == "Yes":
        print("Program Ended")
        break
    elif ask == "No":
        command()
        pass
    else:
        pass
