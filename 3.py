# Finds the largest prime factor of n
# Main code from 'http://stackoverflow.com/questions/14138053/project-euler-3-with-python-most-efficient-method'
# Does not work when n is a square

import time
 
def find_largest_prime_factor(n):
    i = 2
    while i * i < n: # Sieve of Eratosthenes
        while n % i == 0:
            n = n // i
        i += 1
    return n

start_time = time.clock()
n = 600851475143

print (find_largest_prime_factor(n))
print (time.clock() - start_time)
