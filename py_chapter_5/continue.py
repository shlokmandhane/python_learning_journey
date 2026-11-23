#terminates execution in the current iteration and cntinues execution of the loop with the next iteration.

i = 1
while i <= 10 :
    if (i%2 != 0):
        i += 1
        continue
    print(i)
    i += 1    