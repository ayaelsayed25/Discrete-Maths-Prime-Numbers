def sieve_of_eratosthenes(upper_limit):
    # array holding boolean values for whether this number is prime or not
    # all numbers are initially considered prime until they're crossed out
    is_prime = [True for _ in range(upper_limit + 1)]
    # starting from the first prime number we know
    for n in range(2, int(pow(upper_limit, 0.5)) + 1):
        if is_prime[n]:
            for i in range(2 * n, upper_limit + 1, n):
                # crossing out multiples of the prime number
                is_prime[i] = False
    primes = []
    # starting from the first prime number we know
    for p in range(2, upper_limit):
        if is_prime[p]:
            primes.append(p)
    return primes


print(sieve_of_eratosthenes(100))
