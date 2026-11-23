#WAP to print multiplication table of number n.

n = int(input("Enter n:"))

count = 1
while count <= 10 :
    print(n ,"x", count , "=", n*count)
    count += 1