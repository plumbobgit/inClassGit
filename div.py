def div(a):
    for i in range(a):
        divisors = len([i for i in range(1, a+1) if not a % i])
    return divisors
