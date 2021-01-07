def sieve_of_eratosthenes(upper_limit):
    primes = [True for _ in range(upper_limit + 1)]
    for n in range(2, int(pow(upper_limit + 1, 0.5))):
        if primes[n]:
            for i in range(2 * n, upper_limit + 1, n):
                primes[i] = False
    for p in range(2, upper_limit):
        if primes[p]:
            print(p)


sieve_of_eratosthenes(100)
