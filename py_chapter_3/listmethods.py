#List Methods

#Append Method
list = [85, 92, 78, 96]
list.append(88) #Adding an element to the end of the list.
print(list)

#sorting
list = [85, 92, 78, 96, 88]
list.sort() #Sorting the list in ascending order.
print(list)

#sorting in descending order
list = [85, 92, 78, 96, 88]
list.sort(reverse=True) #Sorting the list in descending order.
print(list)

#characters and strings can also be sorted in ascending and descending order.

#reverse method
list = [85, 92, 78, 96, 88]
list.reverse() #Reversing the list.
print(list)

#index method
list = [85, 92, 78, 96, 88]
list.insert(2, 73) #Inserting an element at a specific index.
print(list)

#remove method
list = [85, 92, 78, 96, 88]
list.remove(78) #Removing an element from the list.
print(list)

#pop method
list = [85, 92, 78, 96, 88]
list.pop(3) #Removing the element at index 3 from the list.
print(list)
