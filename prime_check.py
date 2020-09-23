from math import *


def prime(a):
    if a==0 or a==1:
        return False
    if a==2 or a==3:
        return True
    if a%2==0 or a%3==0:
        return False
    for i in range(5,int(sqrt(a))+1,4):
        if a%i==0 or a%(i+2)==0:
            return False
    return True


for _ in range(int(input())):
    n = int(input())
    print(prime(n))
