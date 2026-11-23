#print numbers from 1 to 100.

for i in range(1, 101):
    print(i)


#print numbers from 100 to 1:

for n in range(100, 0, -1):
    print(n)


#print the multiplication table of number n:

n = int(input("Enter n:"))

for t in range(1, 11):
    print(n*t)