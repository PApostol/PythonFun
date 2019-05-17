import math

def get_primes(n):

    if n<2:
        return

    primes = []

    if n>2:
        primes.append(2)

    for num in range(3,n+1,2):

        if all(num%i!=0 for i in range(3, int(math.sqrt(num))+1, 2)):
            primes.append(num)

    return primes