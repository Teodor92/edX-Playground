def isPrime(a):
    if a < 2: return False
    return all(a % i for i in xrange(2, a))

def primesList(N):
    '''
    N: an integer
    Returns a list of prime numbers
    '''
    result = []
    for x in range(2, N + 1):
        if isPrime(x):
            result.append(x)

    return result;