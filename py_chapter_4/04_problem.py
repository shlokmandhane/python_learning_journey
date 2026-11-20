#figure out to store 9 and 9.0 as seperate calues in a set.
#you can take help of built-in data types.

values = {9, "9.0"} #we can use strings method to seperate it.
print(values)

values1 = {
    ("int", 9),
    ("float", 9.0)
}
print(values1)