from math import *
# Calculates fibonacci sequence
def fibonacci(n):
    fibs = [0, 1]
    if n <=0:
        return []
    elif n == 1:
        return fibs[1]
    else:
        for i in range(2, n):
            fibs.append(fibs[-1] + fibs[-2])
        return fibs

n = int(input("How many terms?"))
print(fibonacci(n))
