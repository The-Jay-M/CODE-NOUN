#Generators
#don't allow indexing arbitrary indices like lists
#but can be iterated through using for loops
#and using the yield statement

def countdown():
    i=10
    while i > 0:
        yield i
        i -=1

for i in countdown ():
    print(i)
print("countdown finished!!!")

#yield defines a generator
#replaces the return of a function
#and provides result to it's caller
#without destroying local variables

#generators yield one item at a time
#AND don't have memory restrictions of list so...
#they can be INFINITE!

#def infinite_sevens():
#    while True:
#        yield 7

#for i in infinite_sevens():
#   print(i)



#GENERATING INFINITE PRIMES
#def primes():
#	yield 2
#	cur_primes = [2]
#	n = 2
#	while True:
#		n += 1
#		for p in cur_primes:
#			if n % p == 0:
#				break
#		else:
#			cur_primes.append(n)
#			yield n


#I = primes()
#while True:
#     print(next(I))


#FINITE GENERATOR
def numbers(x):
    for i in range(x):
        if i % 2 == 0:
            yield i

print(list(numbers(11)))


#iterating out a word

def make_word():
    word =""
    for ch in "spam":
        word += ch
        yield word

print(list(make_word()))











