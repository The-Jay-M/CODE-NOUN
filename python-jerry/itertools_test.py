from itertools import count, repeat, cycle, accumulate, takewhile, product
from itertools import permutations
from random import randint
#itertools
#this is a standard library for making iterations
#some itertools functions:
#cycle, count, takewhile, chain, accumulate
#takewhile- takes items from an iterable while predicate function
#remains true
#accumulate- returns a running total of values in an iterable


for i in count(20, -2):
    print(i)
    if i <= 0:
        break

nums= list(accumulate(range(8)))
print(nums)
print(list(takewhile(lambda x: x<=6, nums)))

nums2= [2, 4, 6, 7, 9, 8]
a = takewhile(lambda x: x % 2== 0, nums2)
print(list(a))

letters = ("A", "B", "C")
print(list(product(letters, range(2))))
print(list(permutations(letters, 2)))
