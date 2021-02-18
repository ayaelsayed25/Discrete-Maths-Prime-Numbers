from Sieve_of_Eratosthenes import *
from Miller_Test import *

# list of primes till 100
primes = sieve_of_eratosthenes(100)
for p in primes:
    if miller_test(p, 50):
        print(f'{p} is prime')
    else:
        print(f'{p} is composite')
