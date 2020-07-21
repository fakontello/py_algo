import math

def primes(n):

    sieve = set(range(2, n))
    for i in range(2, int(math.sqrt(n))):
        if i in sieve:
            sieve -= set(range(2*i, n, i))

    return sieve

print(primes(100))
