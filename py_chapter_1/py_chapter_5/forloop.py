#for loops are used for sequential traversal. For transversing list, string, tuples, etc.

veggies = ["potato", "tomato", "brinjal", "cucumber"]

for vegs in veggies:
    print(vegs)


tup = (1, 2, 3, 4, 5, 6)
for num in tup:
    print(num)

name = "shlok"
for char in name:
    if (char == 'o'):
        print("o found")
        break
    print(char)
print("End")
#an optional else can be used in for loop.