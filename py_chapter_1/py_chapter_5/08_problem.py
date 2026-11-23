#WAP to find the factorial of first n numbers using for loop.

n = int(input("Enter n: "))
fact = 1
for nums in range(1, n+1):
    fact *= nums

print("factorial of", n, "is", fact)
    