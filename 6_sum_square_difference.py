def sum_squares(x):
    total = 0
    for i in range(x):
        total += i**2
    return total

def square_sums(y):
    total = 0
    for i in range(y):
        total += i
    return (total**2)

def difference(nums):
    return (square_sums(nums) - sum_squares(nums))

print (difference(101))
