__author__ = 'wnduan'

# Problem Set 1-a From: MIT OPEN COURSEWARE
# Write a program computes and prints 1000th prime number.

# 1. Initialize some state variables:
i = 1  # ith prime number, the program started from 2nd prime number 3.(the 1st one is 2)
n = 1  # generates odd integers
maxI = 2000 #
p = [2,]
total_steps = 0

# def is_prime(n):
#     for i in range(2,n):
#         if n%i == 0:
#             return False
#     return True

# 2. Generate all (odd) integers > 1 as candidates to be prime
while i < maxI:
    n += 2
    is_prime = True
    # 3. For each candidate test wether it's prime:
    for j in p:
        total_steps += 1
        if n%j == 0:
            is_prime = False
            break
    if is_prime:
        i += 1  # the program started from 2nd prime number 3.(the 1st one is 2)
        p.append(n)
        # print '{:d} is the {:d}th prime'.format(n,i)

# 3. Print the results:
print '{:d} is the {:d}th prime'.format(n,i)
print 'total step: {}'.format(total_steps)



# print is_prime(2), 2
# print is_prime(3), 3
# print is_prime(9), 9
