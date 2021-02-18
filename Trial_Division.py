# brute force algorithm, checking every number less than root of n if it's a factor of n or not
def trial_division(n):
    factors = []
    for i in range(2, int(pow(n, 0.5)) + 1):
        while n % i == 0:
            # if i is a factor of n , append it to the factors
            factors.append(i)
            # calculating remainder of n after dividing it by its factor
            n /= i
    # if the list of factors is empty then return true (prime)
    return len(factors) == 0, factors


prime, factor = trial_division(30)
print(prime)
print(factor)
