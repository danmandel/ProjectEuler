# Finds the largest prime factor of n
# Code from stackoverflow
# Does not work for squares

n = 600851475143
i = 2
while i * i < n:
    while n % i == 0:
        n = n // i
    i += 1
print (n)
