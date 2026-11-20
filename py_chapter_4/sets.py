#Set is collection of the unordered item.
#Each element in the set must be unique and immutable.

collection = {1, 2, 2, 3, 3, 3, 3, 4, "hello", "world"}
#it will ignore the duplicate values and will only store unique values in the set.

print(collection)
print(type(collection))
print(len(collection))

collection1 = {} #empty dictionary
print(type(collection)) 

collection2 = set() #empty set
print(type(collection2))
print(collection2)