# Sieve Theorem
# all prime numbers upto n
# (not first n prime numbers)
from math import *

def all_primes(n):
    pr = [True] * (n+1)
    pr[0] = False
    pr[1] = False
    for x in range(2, int(sqrt(n))+1):
        if pr[x] == True:
            for i in range(x*x,n+1,x):
                pr[i] = False
    for i in range(n+1): #changed range value from len(pr) to n+1, confirm if it works properly
        if pr[i] == True:
            print(i, end=" ")

n = int(input())
print(all_primes(n))
