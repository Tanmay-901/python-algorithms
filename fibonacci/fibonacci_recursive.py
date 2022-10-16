def fibonacci(n):
    assert n >= 0 and n == int(n), 'n should be positive integer'
    if n in [0, 1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print("Enter number:", end=" ")
x = int(input())
print(fibonacci(x))
