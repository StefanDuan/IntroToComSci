__author__ = 'wnduan'


def diop(n):
    x,y,z = 6,9,20
    res = []
    for a in range(0,int(n/x)+1):
        for b in range(0,int(n/y)+1):
            for c in range(0,int(n/z)+1):
                print a,b,c,a*x+b*y+c*z
                if a*x+b*y+c*z == n:
                    res.append((a,b,c))
    if len(res) == 0:
        print "No Solution Found"
    else:
        return res

def is_exist(n,pack=(6,9,20)):
    x,y,z = pack
    for a in range(0,int(n/x)+1):
        for b in range(0,int(n/y)+1):
            for c in range(0,int(n/z)+1):
                if a*x+b*y+c*z == n:
                    return True
    return False

def main(pack=(6,9,20)):
    maxNum = 30
    i = 0
    while i <= maxNum:
        is_n = True
        i += 1
        for n in range(i,i+6):
            # print n, 'is', is_exist(n) # For testing and debugging
            if not is_exist(n,pack):
                i = i + (n-i)   # in order to set i to the right number, not to go back
                is_n = False
                break
        if is_n == True:
            print "Given package sizes {}, {}, and {}, the largest number of McNuggets that \
cannot be bought in exact quantity is: {}".format(pack[0],pack[1],pack[2],i-1)
            break
    if i > maxNum:
        print 'No solution found in numbers <', maxNum


# print is_exist(20)
# print diop(20)
main()
main((6,7,15))