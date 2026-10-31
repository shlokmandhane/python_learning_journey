#arithmatic operators

a = 5
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)      #in python, when we divide a number by another, and even if the value is an integer, the answer will be displaed as float.
print(a % b)      #remainder.
print(a ** b)     #'**' is used is 'b' is the power of 'a'.


#relational/comparison operators

a = 50
b = 30

print(a == b)   #this sign is used to check whether it is equal or not. this is especially used in python. answer will be print as a boolean.
print(a != b)   #This sign is used to indicate not equal. answer will be printed in boolean.
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)


#assignment operators

num = 10
#num = num + 10 #10+10 => 20
num += 10
print("num: ", num)

num1 = 5
num1 *= 7
print("num1:", num1)

num2 = 4
num2 /= 2
print("num2:", num2)

num3 = 4
num3 %= 2
print("num3:", num3)

num4 = 10
num4 **= 2
print("num4:", num4)


#logical operators


#logical operators work only on boolean values.
#there are only three logical operators in python, 'not', 'and', and 'or'.

a = 50
b = 30
print(not(a < b))
print(not(a > b))

val1 = True
val2 = False
print("AND operator:", val1 and val2)
print("OR operator:", val1 or val2)

print("OR operator", (a == b) or (a > b))