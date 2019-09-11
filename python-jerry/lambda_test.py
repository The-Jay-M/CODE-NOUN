#named function
def polynomial(x):
    return x**2 + 5*x + 4
print(polynomial(-4))

#lambda
print((lambda x: x**2 + 5*x + 4) (-4))

#here lambda is used as a single line code
#instead of defining the function "polynomial"
#an anonymous function created on fly
#and called with an argument

#(lambda x: x*x)(8)
#returns the square of it's argument


#lambda assigned to variable
#and used like normal function
double = lambda x: x * 2
print (double(7))

#however it's better to define a function
#with def instead, it's just better, ok!

triple = lambda x: x * 3
add= lambda x, y: x + 4
print(add(triple(3), 4))
