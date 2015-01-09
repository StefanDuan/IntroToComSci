##def solve(numLegs, numHeads):
##    for numChicks in range(0, numHeads + 1):
##        numPigs = numHeads - numChicks
##        totLegs = 4*numPigs + 2*numChicks
##        if totLegs == numLegs:
##            return (numPigs, numChicks)
##    return (None, None)
##
####def solve(numLegs, numHeads):
####    pigs, chickens = None, None
####    for numChicks in range(0, numHeads + 1):
####        numPigs = numHeads - numChicks
####        totLegs = 4*numPigs + 2*numChicks
####        if totLegs == numLegs:
####            pigs, chickens = numPigs, numChicks
####    return (pigs, chickens)
##
##def barnYard():
##    heads = int(raw_input('Enter number of heads: '))
##    legs = int(raw_input('Enter number of legs : '))
##    pigs, chickens = solve(legs, heads)
##    if pigs == None:
##        print 'There is no solution'
##    else:
##        print 'Number of pigs: ', pigs
##        print 'Number of chickens: ', chickens

##def huiwen(s):
##    if len(s) <=1:
##        return True
##    else:
##        return s[0] == s[-1] and huiwen(s[1:-1])
##
##def result(s):
##    ans = huiwen(s)
##    if ans:
##        print s, 'is huiwen'
##    else:
##        print s, 'is not huiwen'
##
##def isParlindorm1(s, indent ,level=1):
##    print 'Level', level, indent,  'isParlindorm called with', s
##    if len(s) <= 1:
##        print 'Level', level, indent, 'About to return True from base case'
##        return True
##    else:
##        ans = s[0] == s[-1] and isParlindorm1(s[1:-1], indent+'    ' , level+1)
##        print 'Level', level, indent, 'About to return', ans
##        return ans

def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
