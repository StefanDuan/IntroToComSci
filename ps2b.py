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

def is_exist(n):
    x,y,z = 6,9,20
    for a in range(0,int(n/x)+1):
        for b in range(0,int(n/y)+1):
            for c in range(0,int(n/z)+1):
                if a*x+b*y+c*z == n:
                    return True
    return False

def main():
    maxNum = 200
    i = 0
    while i <= maxNum:
        is_n = True
        i += 1
        for n in range(i,i+6):
            # print n, 'is', is_exist(n) # For testing and debugging
            if not is_exist(n):
                i = i + (n-i)   # in order to set i to the right value, not to go back
                is_n = False
                break
        if is_n == True:
            print "Largest number of McNuggets that cannot be bought in exact quantity: "\
                , i-1
            break


# print is_exist(20)
# print diop(20)
main()