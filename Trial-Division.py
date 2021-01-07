def trial_division(n):
    factors = []
    for i in range(2, int(pow(n, 0.5)) + 1):
        while n % i == 0:
            factors.append(i)
            n /= i
    return len(factors) == 0, factors


prime, factor = trial_division(30)
print(prime)
print(factor)
