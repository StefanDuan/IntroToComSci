# -*- coding: utf-8 -*-
"""
Created on Mon Apr 07 01:31:25 2014

@author: Sifan
"""

x = 1515361
# x = 15
ans = 0

if x >= 0:
    while ans*ans < x:
        ans = ans + 1
    if ans*ans == x:
        print "The square root of %d is %d." % (x, ans)
    else:
        print "%d is not a perfect square." % (x)
else:
    print x, "is negative."