# Fibonacci sequence
def Fibonacci(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return Fibonacci(n-1) + Fibonacci(n-2)

# Find sum of even values that are < 4m   
i=0
result = 0
while Fibonacci(i) < 4000000:
    print Fibonacci(i)
    if Fibonacci(i) % 2 == 0:
        result += Fibonacci(i)
    i += 1
    
print "Result: %d" % result
