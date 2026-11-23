#WAP to search for a number x in this tuple using loop.
# (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = int(input("Enter x:"))

i = 0
while i < len(nums):
    if nums[i] == x:
        print("Found at index", i)
    i += 1