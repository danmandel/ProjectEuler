import time
start_time = time.time()

def SumOfMultiples(a,b,x):
    result = 0
    for i in range(x):
        if (i % a == 0) or (i % b == 0):
            result += i
    return result

print (SumOfMultiples(3,5,1000))
print ("%s seconds" % (time.time() - start_time))
