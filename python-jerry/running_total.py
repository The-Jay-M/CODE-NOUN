def get_running_total(first_number, second_number, third_number):
    return(first_number + second_number + third_number)
print("Welcome to Average Calculator")
print("This is a program to calculate the average of three numbers!")
running_total= 0
first_number= float(input("enter first number: "))
second_number= float(input("enter second number: "))
third_number= float(input("enter third number: "))
running_total= get_running_total(first_number, second_number, third_number)
average = running_total / 3
print ("The average of", first_number, second_number, third_number, "is", average)
