# Eratosthenes application of sieve algorithm
def eratosthenes2(n):
    multiples = set()
    for i in range(2, n+1):
        if i not in multiples:
            yield i
            multiples.update(range(i*i, n+1, i))

primes = list(eratosthenes2(4000000))
