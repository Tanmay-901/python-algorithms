mylist = [1, 2, 3, 4, 5, 7, 8, 9, 10]


def findmissing(ls, n):
    sum1 = (n+1)*n/2
    sum2 = sum(ls)
    print(sum1-sum2)


findmissing(mylist, 10)

