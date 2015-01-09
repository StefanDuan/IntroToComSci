# -*- coding: utf-8 -*-
__author__ = 'wnduan'

# def fib(n):
#     global numCalls
#     numCalls += 1
#     # print 'Call fib with', n
#     if n <= 1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
#
# numCalls = 0
# print fib(30)
# print 'Number of calls:', numCalls
#
# def fast_fib(n,memo):
#     global numCalls
#     numCalls += 1
#     # print 'Call fib with', n
#     if n in memo:
#         return memo[n]
#     else:
#         memo[n] = fast_fib(n-1, memo) + fast_fib(n-2, memo)
#         return memo[n]
#
# def fib1(n):
#     memo = {0:1, 1:1}
#     return fast_fib(n, memo)
#
# numCalls = 0
# print fib1(30)
# print 'Number of calls:', numCalls

def maxVal(w,v,i,aW):
    global numCalls
    numCalls += 1
    if i==0:
        if w[i]<= aW:
            return v[i]
        else:
            return 0
    without_i = maxVal(w,v,i-1,aW)
    if w[i] > aW:
        return without_i
    else:
        with_i = v[i] + maxVal(w,v,i-1,aW-w[i])
    return max(without_i,with_i)

# weights = [1,5,3,4]
# vals = [15,10,9,5]
# numCalls = 0
# res = maxVal(weights,vals,len(weights)-1,8)
# print 'max Val =', res, 'number of calls =', numCalls
#
# weights = [1,1,5,5,3,3,4,4]
# vals = [15,15,10,10,9,9,5,5]
# numCalls = 0
# res = maxVal(weights,vals,len(weights)-1,8)
# print 'max Val =', res, 'number of calls =', numCalls

# maxWeight = 40
# w = [5, 3, 6, 3, 9, 7, 3, 5, 5, 8, 4, 2, 1, 7, 8, 8, 7, 7, 3, 7, 2, 1, 8, 6, 7, 6, 1, 3, 5, 9, 3, 2, 5, 4, 8, 8, 5, 7, 4, 8]
# v = [1, 3, 4, 5, 4, 5, 1, 9, 2, 1, 3, 5, 6, 3, 6, 8, 6, 2, 3, 8, 9, 9, 6, 3, 4, 5, 5, 7, 6, 2, 1, 1, 9, 7, 1, 4, 8, 9, 3, 6]
# numCalls = 0
# res = maxVal(w,v,len(w)-1,maxWeight)
# print 'max Val =', res, 'number of calls =', numCalls

print 'max Val = 88 number of calls = 402140848'

def fastMaxVal(w,v,i,aW,memo):
    global numCalls
    numCalls += 1
    try:
        return memo[(i,aW)]
    except KeyError:
        if i == 0:
            if w[i] <= aW:
                memo[(i,aW)] = v[i]
                return v[i]
            else:
                memo[(i,aW)] = 0
                return 0
        without_i = fastMaxVal(w,v,i-1,aW,memo)
        if w[i] > aW:
            memo[(i,aW)] = without_i
            return without_i
        else:
            with_i = v[i] + fastMaxVal(w,v,i-1,aW-w[i],memo)
        res = max(without_i,with_i)
        memo[(i,aW)] = res
        return res

def maxVal1(w,v,i,aW):
    memo = {}
    return fastMaxVal(w,v,i,aW,memo)

maxWeight = 40
w = [5, 3, 6, 3, 9, 7, 3, 5, 5, 8, 4, 2, 1, 7, 8, 8, 7, 7, 3, 7, 2, 1, 8, 6, 7, 6, 1, 3, 5, 9, 3, 2, 5, 4, 8, 8, 5, 7, 4, 8]
v = [1, 3, 4, 5, 4, 5, 1, 9, 2, 1, 3, 5, 6, 3, 6, 8, 6, 2, 3, 8, 9, 9, 6, 3, 4, 5, 5, 7, 6, 2, 1, 1, 9, 7, 1, 4, 8, 9, 3, 6]
numCalls = 0
res = maxVal1(w,v,len(w)-1,maxWeight)
print 'max Val =', res, 'number of calls =', numCalls