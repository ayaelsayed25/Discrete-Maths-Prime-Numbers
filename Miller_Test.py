import random


def miller_test(n, iterations):
    if n == 2:  # corner case even prime 2
        return True
    if n % 2 == 0:  # if n is even it can't be prime except for 2 handled above
        return False
    m = n - 1
    k = 0
    # finding m where m is the least integer = n-1/2^k
    while m % 2 == 0:
        m //= 2
        k += 1
    # choose a where a is a random number and 1<a<n-1
    for _ in range(iterations):
        prime = False
        a = random.randrange(2, n)
        # according to fermat n is prime if a^(n-1) - 1 mod n = 0
        # we express a^(n-1) - 1 as (a^m-1)(a^m+1)(a^2m)...(a^2)  (difference of squares factorization)
        # if n is divisible by any of the terms in the expansion it's probably prime
        b = pow(a, m, n)
        if b == 1 or b == n - 1:
            # testing divisibility of first two terms (a^m-1),(a^m+1)
            prime = True
        for _ in range(k):
            # testing divisibility of the remaining terms (a^2m)...(a^2)
            b = pow(b, 2, n)
            if b == n - 1:
                prime = True
        if not prime:
            return False
    return True

