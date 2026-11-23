#WAP to find the sum of first n numbers using for loop.

n = int(input("Enter n: "))
sum = 0
for i in range(1, n+1):
    sum += i

print("total sum =", sum)

#WAP to find the sum of first n numbers using while loop.

n1 = int(input("Enter n1: "))
sum = 0
i = 1
while i <= n1:
    sum += i
    i += 1

print("total sum =", sum)
