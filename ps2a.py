__author__ = 'wnduan'

def diop(n):
    x,y,z = 6,9,20
    res = []
    for a in range(0,int(n/x)+1):
        for b in range(0,int(n/y)+1):
            for c in range(0,int(n/z)+1):
                if a*x+b*y+c*z == n:
                    res.append((a,b,c))
    if len(res) == 0:
        print "No Solution Found"
    else:
        return res


print diop(48)