# returns list with prime factors of n
from math import sqrt
import time

def timing(func):
    def wrapper(*arg, **kw):
        start = time.time()
        ans = func(*arg, **kw)
        stop = time.time()
        print('Time taken: {:0.2f} s'.format(stop - start))
        return ans
    return wrapper


@timing
def prime_factors(n): 
    factors = []
    while n % 2 == 0:
        n = n // 2
        factors.append(2)
          
    for i in range(3,int(sqrt(n))+1,2): 
        while n % i== 0: 
            n = n // i
            factors.append(i)
              
    if n > 2: 
        factors.append(n)
    
    return factors


@timing
def prime_factors2(n):
    i = 2
    factors = []

    while i * i <= n:
        if n % i:
            i += 1
        else:
            n = n//i
            factors.append(i)

    if n > 1:
        factors.append(n)

    return factors


# driver code
n=18014398241046564

print(prime_factors(n))
print(prime_factors2(n))
