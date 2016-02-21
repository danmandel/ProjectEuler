# Finds the largest prime factor of n
# Main code from stackoverflow
# Does not work for squares

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
