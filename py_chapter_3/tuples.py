#tuples aare similar to lists.
#tuples are immutable, meaning they cannot be changed after creation.
#tuples are defined using parentheses () instead of square brackets [].

tup = (1, 2, 3, 4, 5, 2, 2)
print(type(tup))
print(tup[0])
print(tup[3])

tup1 = (1, )
print(type(tup1)) #this is a tuple with a single element, note the comma.
print(tup1[0])
print(tup[1:4]) #slicing works the same way as lists.
print(tup.index(3)) #returns the index of the first occurrence of the value 3.
print(tup.count(2)) #returns the number of occurrences of the value 2 in the tuple.