#print the elements of the following list using for loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for num in nums:
    print(num)


#search for a number in this tuple using for loop:
# tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 49

idx = 0
for el in tup:
    if (el == x):
        print("number found at idx", idx)
    idx += 1 

#this is known as linear search.