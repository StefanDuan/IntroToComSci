__author__ = 'wnduan'

# Problem Set 1-b From: MIT OPEN COURSEWARE
# Write a program computes and prints sum.

import math
# 1. Initialize some state variables:
i = 1  # ith prime number, the program started from 2nd prime number 3.(the 1st one is 2)
n = 1  # generates odd integers
N = 300 #
total_steps = 0
log_sum = math.log(2)

# def is_prime(n):
#     for i in range(2,n):
#         if n%i == 0:
#             return False
#     return True

# 2. Generate all (odd) integers > 1 as candidates to be prime
while True:
    n += 2
    is_prime = True
    # 3. For each candidate test wether it's prime:
    for j in range(3,int(math.sqrt(n))+1,2):
        total_steps += 1
        if n%j == 0:
            is_prime = False
            break
    if is_prime:
        i += 1  # the program started from 2nd prime number 3.(the 1st one is 2)
        log_sum += math.log(n)
        print '{:d} is the {:d}th prime, sum={}'.format(n,i,log_sum)


# 3. Print the results:
print 'sum \t n \t sum/n'
print '{} \t {} \t {}'.format(log_sum,n,log_sum/n)
# print 'total step: {}'.format(total_steps)



# print is_prime(2), 2
# print is_prime(3), 3
# print is_prime(9), 9
