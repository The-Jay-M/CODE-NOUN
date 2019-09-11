#SETS
#sets are data structures similar to lists or dictionaries
#sets share some functionality with lists
#sets are created with curly braces or the set function

num_set = {1, 2, 3, 4, 5}
word_set = set(["spam", "eggs", "sausage"])
print (3 in num_set)
print ("spam" not in word_set)

#use set() to make an empty set
#set{} makes a dictionary
#sets cannot contain duplicate elements
#sets are unordered. Hence they can't be indexed
#It's faster to check if an item is part of a set
#than part of a list
#use add rather than append
#the method remove removes a specific element
#pop removes arbitrary element
#len  is one of several operations shared with lists

nums = {1, 2, 1, 3, 1, 4,  5, 6}
words= {"eggs", "spam", "white", "blue", "red"}
print(nums)
print(nums | words)
print(nums & words)
print(nums - words)

nums.add("white")
nums.remove(3)
print(len(nums))
print(nums)
print(nums & words)
print(nums - words)
print(words -nums)
print(words)

#basic uses of sets are membership testing
#and elimination of duplicate entries
