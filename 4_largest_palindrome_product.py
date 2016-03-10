# Find the largest palindrome made from the product of two 3 digit numbers
# Ex. 91x99 = 9009

import time

def find_palindrome(): # Paldindrome from product of a*b
    largest_product = 0  
    for a in range(999,100,-1):
        for b in range(a,100,-1):           
            product = a * b
            if product > largest_product:
                if str(product) == str(product)[::-1]:
                    largest_product = product
                    
    return largest_product

start_time = time.clock()
print (find_palindrome())     
print (time.clock() - start_time)

