#WAP to check if a list contains palindrome of elements.

list1 = [1,2,1]
list2 = [1,2,3]

copy_list1 = list1.copy() #Creating a copy of the original list.
copy_list1.reverse() #Reversing the copy of the list.

copy_list2 = list2.copy()
copy_list2.reverse()

if(copy_list1 == list1):
    print("list1 is a palindrome.")
else:
    print("list1 is not a palindrome.")

if(copy_list2 == list2):
    print("list2 is a palindrome.")
else:
    print("list2 is not a palindrome.")
