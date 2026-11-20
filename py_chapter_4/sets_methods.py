#sets are mutable but elements in sets are immutable. Sets are unordered and do not allow duplicate elements.
#set.add(el). adds an element.

collection = set()
collection.add(5)
collection.add(8)
collection.add(18)
collection.add("Shlok")
print(collection)
#we can add tuples in the set but we cannot add lists or dictionaries as they are mutable.

#set.remove(el). removes an element.
collection.remove(5)
print(collection)

#set.clear(). removes all elements from the set.
collection.clear()
print(collection)
print(len(collection))

#set.pop(). removes a random element from the set.
collection1 = {1, 2, 2, 3, 3, 3, 3, 4, "hello", "world"}
print(collection1.pop())
print(collection1.pop())

#set.union(set1, set2). returns a new set with all elements from both sets.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1.union(set2))

#set.intersection(set1, set2). returns a new set with only the elements that are common to both sets.
print(set1.intersection(set2))