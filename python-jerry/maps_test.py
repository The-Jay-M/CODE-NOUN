#on maps

def add_five(x):
    return x + 5

nums = [11, 22, 33, 44, 55]
result=list(map(add_five, nums))
print(result)

#more easily done with lambda

nums1= [11, 22, 33, 44, 55]

result= list(map(lambda x: x+5, nums))
print(result)

#on filter

nums = [11, 22, 33, 44, 55]
res = list(filter(lambda x: x%2==0, nums))
print(res)

#as seen filter filters an iterable (list)
#by removing items not matching a predicate

#filtering greater than 5...
#extracting less than 5...
nums = [1, 2, 3, 5, 6, 33, 44, 6, 0]
res= list(filter(lambda x: x<5, nums))
print(res)
