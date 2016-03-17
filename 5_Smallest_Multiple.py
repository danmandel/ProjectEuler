#2520 is the smallest number than can be divided by each of the numbers
#from 1 to 10 without any remainder

import time
nums = [11,12,13,14,15,16,17,18,19,20]
def is_divisible_by(x,nums):
    for i in nums:
        if x % i != 0:
            return False
            print ("false: ",x)
    return True
    


def test1():
    for x in range (1,300000000):
        if is_divisible_by(x,nums):
            print ("is divisible by: ",x)
            break
        

start = time.time()
test1()
end = time.time()
duration = end-start
print (duration)
