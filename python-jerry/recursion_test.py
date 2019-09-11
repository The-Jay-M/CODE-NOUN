#RECURSION
#functions calling themselves
#below is factorial recursion
#base case acts as exit condition
#base case in factorial is 1! = 1

def factorial(x):
    assert x >= 0, "Enter a POSITIVE NUMBER"
    assert round(x)==x, "Enter an INTEGER"
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)

print(factorial(4.0))


#if base case is omitted
#RuntimeError occurs
#because it becomes infinite
#and interpreter runs out of memory and crashes
def factorial(x):
    return x * factorial(x-1)

#print(factorial(4.0))


#INDIRECT RECURSION
def is_even(x):
    if x == 0:
      return True
    else:
        print(x)
        return is_odd(x-1)
def is_odd(x):
    return not is_even(x)

#print(is_odd(17))
#print(is_even(17))


#this case

def fib(x):
    if x == 0 or x ==1:
        return 1
    else:
        print(x)
        return fib(x-1) + fib(x-2)
print(fib(0))

#2 3
#2* f(2,2)
#2* (2 * f(2,1))
#2* (2* (2* f(2,0)))
#2* (2* (2 * 1)) = 8

def power(x, y):
    if y == 0:
        return 1
    else:
        return x * power(x, y-1)
print(power(2, 3))


a = (lambda x: x * (x + 1))(6)
print(a)





































            
